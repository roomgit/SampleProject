#1
#from tkinter import Tk, ttk, PhotoImage
import tkinter as tk
#root = tk.Tk()

class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.img = tk.PhotoImage(file='nanohana.gif')
        label = tk.Label(self, image=self.img)
        label.pack()
        self.img2 = tk.PhotoImage(file='happy.gif')
        label = tk.Label(self, image=self.img2)
        label.pack()



if __name__ == "__main__":
    #root.mainloop()
    f = Frame()
    f.pack()
    f.mainloop()


