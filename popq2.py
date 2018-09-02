# switchface.py
from tkinter import Button, Frame
from PIL.Image import open
from PIL.ImageTk import PhotoImage

class switchface(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        # The pic currently displayed.
        self.current = 0
        # Open the images.
        self.i0 = open("happy.gif")
        self.i1 = open("nanohana.gif")
        # Make them tkinter-compatible.
        self.p0 = PhotoImage(self.i0)
        self.p1 = PhotoImage(self.i1)

        # Create button, add image.
        self.b = Button(master, image=self.p0, command=self.switch)
        self.b.pack()
        # Keep a reference.
        self.b.image = self.p0

    def switch(self):
        if (self.current == 0):
            self.b.configure(image=self.p1)
            self.current = 1
        else:
            self.b.configure(image=self.p0)
            self.current = 0

if __name__== "__main__":
    switchface().mainloop()