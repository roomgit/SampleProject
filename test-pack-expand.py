from tkinter import *

root = Tk()

w = Label(root, text="Red", bg="red", fg="white")
w.pack(fill=BOTH, expand=0)
w = Label(root, text="Green", bg="green", fg="black")
w.pack(fill=BOTH)
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack(fill=BOTH)

mainloop()