# popq3.py
import tkinter as tk
#from PIL.Image import open
#from PIL.ImageTk import PhotoImage

class switchface(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        # The pic currently displayed.
        self.current = 0
        # Open the images.
        #self.i0 = open("happy.gif")
        #self.i1 = open("nanohana.gif")
        # Make them tkinter-compatible.
        self.p0 = tk.PhotoImage(file='happy.gif')
        self.p1 = tk.PhotoImage(file='./resource/nanohana.png')

        # Create button, add image.
#        self.b = tk.Button(master, image=self.p0, command=self.switch)
        self.b = tk.Button(master, text="ボタン", image=self.p0)
        self.b.bind("<Button-1>", self.callback)   # Button-1 : マウス左ボタン(押され）
        self.b.bind("<ButtonRelease-1>", self.callback2)
        self.b.pack()
        # Keep a reference.
        self.b.image = self.p0

    def callback(self, event):      # この（"self" と"イベント"の２個が重要）
        print(event.widget["text"])
        self.b.configure(image=self.p1)

    def callback2(self, event):  # この（"self" と"イベント"の２個が重要）
        print(event.widget["text"], "released")
        self.b.configure(image=self.p0)

'''
    def switch(self):
        if (self.current == 0):
            self.b.configure(image=self.p1)
            self.current = 1
        else:
            self.b.configure(image=self.p0)
            self.current = 0
'''


if __name__== "__main__":

    switchface().mainloop()