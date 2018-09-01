from tkinter import Tk, ttk, PhotoImage

root = Tk()

img = PhotoImage(file='nanohana.gif')

label = ttk.Label(root, image=img)
label.grid()
root.mainloop()