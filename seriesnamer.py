#!/usr/bin/env python3
import curses
import curses.textpad
import argparse
import os.path
import math

from column import Column
import pattern
import keyvalueextractor

# todo:
# set cell value for current cell
# set cell value for current column for all selected rows
# apply formatting function for current column for all selected rows
# save current files in json
# provide better editing experince with shortcut hints
# provide better editing experince when entering key value extractor pattern (live extract)
# provide a way to inspect pattern errors
# allow editing already entered pattern
# gather data from external sources like imdb, tvdb and others
# move files function
# perhaps move from curses to https://github.com/urwid/urwid and the table widget from https://github.com/ragardner/tksheet
# save common extraction patterns and "auto extract" smartly
# add/remove to selection with missing/has value, regex file/value matching
# auto add columns based on rows
# change column title and sort
# imdb lookup and create nfo file for "xmdb"


def hint(stdscr, t):
    height = 1
    width = len(t) + 1
    wh, ww = stdscr.getmaxyx()
    y = int(math.floor(wh/2))-1
    x = int(math.floor((ww - width)/2))
    curses.textpad.rectangle(stdscr, y-1, x-1, y+height, x+width+1)
    stdscr.addstr(y, x, ' {} '.format(t))


def message(stdscr, text):
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height-1, 10, '{}'.format(text))
    stdscr.getch()


class TextboxCallback(curses.textpad.Textbox):
    def __init__(self, win, callback):
        super().__init__(win)
        self.callback = callback
        self.win = win

    def do_command(self, ch):
        r = super().do_command(ch)
        # gather always places cursor at the end
        # you can use stdscr.getyx() and stdscr.move(y,x) 
        cy, cx = self.win.getyx() 
        content = self.gather()
        self.win.move(cy,cx) 
        self.callback(content, self.win)
        return r


def text_input(stdscr, title):
    stdscr.addstr(0, 0, "{}: (hit Ctrl-G to send)".format(title))

    height = 1
    width = 60
    y = 2
    x = 1

    editwin = curses.newwin(height, width, y, x)
    curses.textpad.rectangle(stdscr, y-1, x-1, 1+height+1, 1+width+1)
    stdscr.refresh()

    curses.curs_set(1)
    box = curses.textpad.Textbox(editwin)
    box.edit()
    curses.curs_set(0)
    return box.gather()


def text_input_callback(stdscr, title, callback):
    stdscr.addstr(0, 0, "{}: (hit Ctrl-G to send)".format(title))

    height = 1
    width = 60
    y = 2
    x = 1

    editwin = curses.newwin(height, width, y, x)
    def render():
        curses.textpad.rectangle(stdscr, y-1, x-1, 1+height+1, 1+width+1)
        stdscr.refresh()
    render()

    curses.curs_set(1)
    box = TextboxCallback(editwin, lambda text, win: callback(text, win, render))
    box.edit()
    curses.curs_set(0)
    return box.gather()


class Option:
    def __init__(self, name, key, callback):
        self.name = name
        self.key = key
        self.callback = callback


def menu(options):
    text = ' '.join(opt.name for opt in options)
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height-1, 10, '{}'.format(text))
    key = stdscr.getch()
    for opt in options:
        if opt.key == key:
            opt.callback()

TABLE_INPUT_Y = 6

class FilterDialog:
    def __init__(self, stdscr, src_data, prop):
        self.stdscr = stdscr
        self.src_data = src_data
        self.prop = prop
        self.kve = None
        self.files = [d[prop] for d in src_data]
        self.highlight_index = 0

    def render_table(self, kve, starty):
        startx = 2
        nextx = 0

        for row_index, f in enumerate(files):
            display = f[:10]
            stdscr.addstr(row_index+starty + 1, startx, display)
            nextx = max(nextx, startx + len(display) + 1)

        startx = nextx
        nextx = 0

        if kve is not None:
            for col_index, col in enumerate(kve.get_keys()):
                stdscr.addstr(starty, startx, col, curses.A_REVERSE)
                nextx = max(nextx, startx + len(col) + 1)
                for row_index, f in enumerate(files):
                    try:
                        ex, err = kve.extract(f)
                        display = ex[col] if col in ex else ''
                        stdscr.addstr(row_index+starty + 1, startx, display)
                        nextx = max(nextx, startx + len(display) + 1)
                    except keyvalueextractor.FormatError:
                        pass
                startx = nextx
                nextx = 0

    def render_highlight(self):
        stdscr.addstr(TABLE_INPUT_Y - 2, 2, files[highlight_index])

    def on_input(self, input, win, render):
        kve = None
        try:
            kve = keyvalueextractor.Compile(input)
        except keyvalueextractor.FormatError:
            pass
        stdscr.clear()
        render_highlight()
        render_table(kve, TABLE_INPUT_Y)
        render()
        win.redrawwin()
        win.refresh()

    def run_dialog(self):
        run = True
        while run:
            if kve is None:
                stdscr.clear()
                render_highlight()
                render_table(kve, TABLE_INPUT_Y)
                stdscr.refresh()

                k = text_input_callback(stdscr, 'Enter pattern', on_input)
                # k = text_input(stdscr, 'Enter pattern')
                try:
                    kve = keyvalueextractor.Compile(k)
                except keyvalueextractor.FormatError:
                    message(stdscr, 'format error')
            stdscr.clear()
            render_table(kve, 0)
            stdscr.refresh()
            # menu([Option('Extract', ord('e'), lambda: kve = None),
            input = stdscr.getch()
            if input == ord('e'):
                kve = None
            elif input == ord('r'):
                for src in src_data:
                    f = src[prop]
                    ex, _ = kve.extract(f)
                    for col in kve.get_keys():
                        display = ex[col] if col in ex else ''
                        src[col] = display
                run = False
            elif input == ord('q'):
                run = False
            else:
                message(stdscr, 'unknown new input: {}'.format(input))


def filter_dialog(stdscr, src_data, prop):
    dialog = FilterDialog(stdscr, src_data, prop)
    if len(dialog.files) == 0:
        message(stdscr, 'no files to process')
        return

    dialog.run_dialog()


def gui(stdscr, args):
    run = True
    current_row = 0
    current_col = 0
    curses.curs_set(0)

    datas = [{'file': f} for f in args.files]
    selected = [False for d in datas]
    columns = [Column('File', '$file_base(%file%)')]
    functions = pattern.DefaultFunctions()
    functions['file_base'] = lambda args: os.path.basename(args[0])

    while run:
        stdscr.clear()
        startx = 2
        starty = 0
        nextx = 0
        for row_index, sel in enumerate(selected):
            if sel:
                stdscr.addstr(row_index+starty+1, 0, 'x')
        for col_index, col in enumerate(columns):
            stdscr.addstr(starty, startx, col.title, curses.A_REVERSE)
            nextx = max(nextx, startx + len(col.title) + 1)
            for row_index, data in enumerate(datas):
                display = col.get_display(functions, data)
                if row_index == current_row and col_index == current_col:
                    display = '[{}]'.format(display)
                else:
                    display = ' {} '.format(display)
                stdscr.addstr(row_index+starty + 1, startx, display)
                nextx = max(nextx, startx + len(display) + 1)
            startx = nextx
            nextx = 0

        stdscr.refresh()
        input = stdscr.getch()
        if input == ord('q'):
            run = False
        elif input == ord('a'):
            selected = [False for _ in selected]
        elif input == ord('A'):
            selected = [True for _ in selected]
        elif input == ord(' '):
            selected[current_row] = not selected[current_row]
        elif input == ord('e'):
            s = [d for s, d in zip(selected, datas) if s]
            if len(s) == 0:
                message(stdscr, 'no files selected')
            else:
                filter_dialog(stdscr, s, 'file')
        elif input == ord('n'):
            hint(stdscr, 'new Column...')
            input = stdscr.getch()
            if input == ord('c'):
                p = text_input(stdscr, "column format")
                c = Column(p, p)
                columns.append(c)
            else:
                message(stdscr, 'unknown new input: {}'.format(input))
        elif input == ord('k'):
            # go up
            current_row -= 1
            if current_row < 0:
                current_row = len(datas) - 1
        elif input == ord('j'):
            # go down
            current_row += 1
            if current_row >= len(datas):
                current_row = 0
        elif input == ord('h'):
            # go left
            current_col -= 1
            if current_col < 0:
                current_col = len(columns) - 1
        elif input == ord('l'):
            # go right
            current_col += 1
            if current_col >= len(columns):
                current_col = 0
        elif input == curses.KEY_HOME:
            current_row = 0
            current_col = 0
        else:
            message(stdscr, 'unknown input: {}'.format(input))


def main():
    parser = argparse.ArgumentParser(description='sort files')
    parser.add_argument('files', metavar='F', nargs='+', help='files to sort')
    args = parser.parse_args()
    curses.wrapper(gui, args)

if __name__ == "__main__":
    main()
