#1
#from tkinter import Tk, ttk, PhotoImage
import tkinter as tk
root = tk.Tk()

img = tk.PhotoImage(file='nanohana.gif')
img2 = tk.PhotoImage(file='happy.gif')
label = tk.Label(root, image=img)
label2 = tk.Label(root, image=img2)
label.grid()
label2.grid()
root.mainloop()