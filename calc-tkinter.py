# -*- coding: utf-8 -*-

import tkinter as tk

class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master,  width=200, height=150)
        self.master.title('Calc')

        #root = tk.Tk()
        self.contentVar = tk.StringVar(self,'')
        contentEntry = tk.Entry(self, textvariable=self.contentVar)
        contentEntry['state'] = 'readonly'
        contentEntry.place(x=10, y=10, width=180, height=20)

        numberbuttons = []


        for i in range(10):
            button = tk.Button(self, text=str(i), font=('Calibri', 16))
            numberbuttons.append(button)



        numberbuttons[0].place(x=10, y=100, width=30, height=20)
        numberbuttons[1].place(x=10, y=80, width=30, height=20)
        numberbuttons[2].place(x=40, y=80, width=30, height=20)
        numberbuttons[3].place(x=70, y=80, width=30, height=20)
        numberbuttons[4].place(x=10, y=60, width=30, height=20)
        numberbuttons[5].place(x=40, y=60, width=30, height=20)
        numberbuttons[6].place(x=70, y=60, width=30, height=20)
        numberbuttons[7].place(x=10, y=40, width=30, height=20)
        numberbuttons[8].place(x=40, y=40, width=30, height=20)
        numberbuttons[9].place(x=70, y=40, width=30, height=20)

        period = tk.Button(self, text='.', font=('Calibri', 16))
        period.place(x=40, y=100, width=30, height=20)

        equal = tk.Button(self, text='=', font=('Calibri', 16))
        equal.place(x=70, y=100, width=30, height = 20)

        plus = tk.Button(self, text='+', font=('Calibri', 16))
        plus.place(x=100, y=40, width=30, height=20)

        minus = tk.Button(self, text='-', font=('Calibri', 16))
        minus.place(x=100, y=60, width=30, height=20)

        multiply = tk.Button(self, text='*', font=('Calibri', 16))
        multiply.place(x=100, y=80, width=30, height=20)

        divide = tk.Button(self, text='/', font=('Calibri', 16))
        divide.place(x=100, y=100, width=30, height=20)

        all_clear = tk.Button(self,text='C', font=('Calibri',16))
        all_clear.place(x=130, y=40, width=30, height=20)

'''
        numberbuttons[0].grid(row=5, column=0)
        numberbuttons[1].grid(row=2, column=0)
        numberbuttons[2].grid(row=2, column=1)
        numberbuttons[3].grid(row=2, column=2)
        numberbuttons[4].grid(row=3, column=0)
        numberbuttons[5].grid(row=3, column=1)
        numberbuttons[6].grid(row=3, column=2)
        numberbuttons[7].grid(row=4, column=0)
        numberbuttons[8].grid(row=4, column=1)
        numberbuttons[9].grid(row=4, column=2)

'''



if __name__ == "__main__":
    f = window()
    f.pack()
    f.mainloop()

