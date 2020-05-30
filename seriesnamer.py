#!/usr/bin/env python3
import curses
import curses.textpad
import argparse
import os.path

from column import Column
import pattern


def hint(stdscr, t):
    height = 1
    width = len(t) + 1
    y = 2
    x = 1
    curses.textpad.rectangle(stdscr, y-1, x-1, 1+height+1, 1+width+1)
    stdscr.addstr(y, x, ' {} '.format(t))


def message(stdscr, text):
    height, width = stdscr.getmaxyx()
    stdscr.addstr(height-1, 10, '{}'.format(text))
    stdscr.getch()


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
        # This raises ZeroDivisionError when i == 10.
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
        elif input == ord(' '):
            selected[current_row] = not selected[current_row]
        elif input == ord('n'):
            hint(stdscr, 'New column...')
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
