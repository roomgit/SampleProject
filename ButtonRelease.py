# -*- coding: utf-8 -*-

#widget上で左ボタンを放した時にその座標を表示する。

from tkinter import *

root = Tk()

def callback(event):
    print ("ButtonReleased at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<ButtonRelease-1>", callback)
frame.pack()

root.mainloop()