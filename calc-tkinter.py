# -*- coding: utf-8 -*-

import tkinter as tk

class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master,  width=400, height=150)
        self.master.title('Calc')

        #root = tk.Tk()
        self.contentVar = tk.StringVar(self,'')
        contentEntry = tk.Entry(self, textvariable=self.contentVar)
        contentEntry['state'] = 'readonly'
        contentEntry.place(x=10, y=10, width=180, height=20)

        self.p0 = tk.PhotoImage(file='./resource/Press_0.png')
        self.p1 = tk.PhotoImage(file='./resource/Press_1.png')
        self.p2 = tk.PhotoImage(file='./resource/Press_2.png')
        self.p3 = tk.PhotoImage(file='./resource/Press_3.png')
        self.p4 = tk.PhotoImage(file='./resource/Press_4.png')
        self.p5 = tk.PhotoImage(file='./resource/Press_5.png')
        self.p6 = tk.PhotoImage(file='./resource/Press_6.png')
        self.p7 = tk.PhotoImage(file='./resource/Press_7.png')
        self.p8 = tk.PhotoImage(file='./resource/Press_8.png')
        self.p9 = tk.PhotoImage(file='./resource/Press_9.png')
        self.pperiod = tk.PhotoImage(file='./resource/Press_period.png')
        self.pequal = tk.PhotoImage(file='./resource/Press_equal.png')
        self.pplus = tk.PhotoImage(file='./resource/Press_plus.png')
        self.pminus = tk.PhotoImage(file='./resource/Press_minus.png')
        self.pmultiply = tk.PhotoImage(file='./resource/Press_multiply.png')
        self.pdivide = tk.PhotoImage(file='./resource/Press_divide.png')
        self.pall_clear = tk.PhotoImage(file='./resource/Press_AC.png')

        numberbuttons = []
        for i in range(10):
            button = tk.Button(self, text=str(i), font=('Calibri', 16),bd=0)
            button
            numberbuttons.append(button)

        numberbuttons[0].configure(image=self.p0)
        numberbuttons[1].configure(image=self.p1)
        numberbuttons[2].configure(image=self.p2)
        numberbuttons[3].configure(image=self.p3)
        numberbuttons[4].configure(image=self.p4)
        numberbuttons[5].configure(image=self.p5)
        numberbuttons[6].configure(image=self.p6)
        numberbuttons[7].configure(image=self.p7)
        numberbuttons[8].configure(image=self.p8)
        numberbuttons[9].configure(image=self.p9)


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




        period = tk.Button(self, text='.', font=('Calibri', 16),bd=0)
        period.configure(image=self.pperiod)
        period.place(x=40, y=100, width=30, height=20)

        equal = tk.Button(self, text='=', font=('Calibri', 16),bd=0)
        equal.configure(image=self.pequal)
        equal.place(x=70, y=100, width=30, height = 20)

        plus = tk.Button(self, text='+', font=('Calibri', 16),bd=0)
        plus.configure(image=self.pplus)
        plus.place(x=100, y=40, width=30, height=20)

        minus = tk.Button(self, text='-', font=('Calibri', 16),bd=0)
        minus.configure(image=self.pminus)
        minus.place(x=100, y=60, width=30, height=20)

        multiply = tk.Button(self, text='*', font=('Calibri', 16),bd=0)
        multiply.configure(image=self.pmultiply)
        multiply.place(x=100, y=80, width=30, height=20)

        divide = tk.Button(self, text='/', font=('Calibri', 16),bd=0)
        divide.configure(image=self.pdivide)
        divide.place(x=100, y=100, width=30, height=20)

        all_clear = tk.Button(self,text='C', font=('Calibri',16),bd=0, relief='flat')
        all_clear.configure(image=self.pall_clear)
        all_clear.place(x=130, y=40, width=96, height=51)
        all_clear.bind("<Button-1>", self.all_clear_press)

    def all_clear_press(self, event):
        print(event.widget["text"])
        event.widget.configure(image=self.p0)


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

