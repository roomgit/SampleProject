import tkinter as tk

class MyApp:
    def __init__(self, master):
        self.l = tk.Label(master,text="My Button")
        self.l.pack()

        self.b = tk.Button(master, text= "Hello", command = self.hello)
        #self.img = tk.PhotoImage(file='nanohana.gif')
        #self.l.configure(img=self.img)
        self.b.pack()


    def hello(self):
        print ("Hello")

    #def loadimage(self):
