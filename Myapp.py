import tkinter as tk


class MyApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.lbl = tk.Label(self, text="My Button")
        self.lbl.pack()

        self.btn = tk.Button(self, text="Hello", command=self.hello)
        self.btn.pack()

    def hello(self):
        print("Hello")


