#1
#from tkinter import Tk, ttk, PhotoImage
import tkinter as t
root = t.Tk()

img = t.PhotoImage(file='nanohana.gif')

label = t.Label(root, image=img)
label.grid()
root.mainloop()