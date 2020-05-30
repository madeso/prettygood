#!/usr/bin/env python3

# helpful doc: https://tkdocs.com/tutorial/onepage.html

from tkinter import *
from tkinter import ttk

if __name__ == "__main__":
    root = Tk()
    ttk.Button(root, text="Hello World").grid()
    root.mainloop()

