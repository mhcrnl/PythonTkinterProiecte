#!/usr/bin/python
# write tkinter as Tkinter to be Python 2.x compatibel

from Tkinter import *

def hello(event):
    print("Single click, Button-1")

def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

    widget = Button(None, text="Mouse clicks")
    widget.pack()
    widget.bind('<Button-1>', hello)
    widget.bind('<Double-1>', quit)

    widget.mainloop()
    widget.destroy()

