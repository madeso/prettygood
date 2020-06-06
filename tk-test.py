#!/usr/bin/env python3

# helpful doc: https://tkdocs.com/tutorial/onepage.html
# table https://github.com/ragardner/tksheet
# https://stackoverflow.com/questions/9348264/does-tkinter-have-a-table-widget
# styling tkinter https://www.youtube.com/watch?v=oV68QJJUXTU


from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
    root = Tk()
    ttk.Button(root, text="Hello World").grid()
    root.mainloop()

