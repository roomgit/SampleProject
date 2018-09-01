#1
#from tkinter import Tk, ttk, PhotoImage
import tkinter as tk
root = tk.Tk()

img = tk.PhotoImage(file='nanohana.gif')

label = tk.Label(root, image=img)
label.grid()
root.mainloop()