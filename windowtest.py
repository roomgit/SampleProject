import tkinter as tk


class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.b = tk.Button(master, text="button1",  command=self.calc) # command による呼び出し
        self.b.pack()
        self.lbs = tk.StringVar()
        self.entry = tk.Entry(self, width=7, textvariable=self.lbs)
        self.entry.pack(side=tk.LEFT)
        self.label = tk.Label(self, width=7, text="result", font=('Helvetica', '16')) # Font はタプルで指定できる
        self.label.pack()
        self.label2 = tk.Label(self, width=7, text="Label2", font=('Helvetica', '16')) # Font はタプルで指定できる
        self.label2.pack()
    def calc(self):
        try:
            value = float(self.lbs.get())
            print("The number of kgs is ", 0.453592 * value)
            self.label.configure(text=0.453592 * value)    # Label のテキストに数値をそのまま放り込むと変換してくれる
            self.label2.configure(text=)


        except ValueError:
            pass
if __name__ == "__main__":
    window().mainloop()