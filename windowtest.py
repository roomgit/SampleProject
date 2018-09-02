import tkinter as tk


class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.b = tk.Button(master, text="button1",  command=self.calc)
        self.b.pack()
        self.lbs = tk.StringVar()
        self.entry = tk.Entry(self, width=7, textvariable=self.lbs)
        self.entry.pack(side=tk.LEFT)
        self.label = tk.Label(self, width=7, text="result")
        self.label.pack()

    def calc(self):
        try:
            value = float(self.lbs.get())
            print("The number of kgs is ", 0.453592 * value)
            self.label.configure(text=0.453592 * value)    # Label のテキストに数値をそのまま放り込むと変換してくれる



        except ValueError:
            pass
if __name__ == "__main__":
    window().mainloop()