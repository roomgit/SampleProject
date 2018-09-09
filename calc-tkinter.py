# -*- coding: utf-8 -*-

import tkinter as tk

class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master,  width=600, height=375)

        self.img = tk.PhotoImage(file='./resource/background.png')
        label = tk.Label(self, image=self.img)
        label.place(x=0, y=0, width=600, height=375)

        self.master.title('Calc')
        self.master.resizable(False, False)

        # Display contents
        contentVar = tk.StringVar(self,'')
        contentEntry = tk.Entry(self, textvariable=contentVar)
        #contentEntry['state'] = 'readonly'
        contentEntry.place(x=250, y=30, width=300, height=60)

        # Buttons
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
        self.r0 = tk.PhotoImage(file='./resource/Release_0.png')
        self.r1 = tk.PhotoImage(file='./resource/Release_1.png')
        self.r2 = tk.PhotoImage(file='./resource/Release_2.png')
        self.r3 = tk.PhotoImage(file='./resource/Release_3.png')
        self.r4 = tk.PhotoImage(file='./resource/Release_4.png')
        self.r5 = tk.PhotoImage(file='./resource/Release_5.png')
        self.r6 = tk.PhotoImage(file='./resource/Release_6.png')
        self.r7 = tk.PhotoImage(file='./resource/Release_7.png')
        self.r8 = tk.PhotoImage(file='./resource/Release_8.png')
        self.r9 = tk.PhotoImage(file='./resource/Release_9.png')
        self.rperiod = tk.PhotoImage(file='./resource/Release_period.png')
        self.requal = tk.PhotoImage(file='./resource/Release_equal.png')
        self.rplus = tk.PhotoImage(file='./resource/Release_plus.png')
        self.rminus = tk.PhotoImage(file='./resource/Release_minus.png')
        self.rmultiply = tk.PhotoImage(file='./resource/Release_multiply.png')
        self.rdivide = tk.PhotoImage(file='./resource/Release_divide.png')
        self.rall_clear = tk.PhotoImage(file='./resource/Release_AC.png')

        numberbuttons = []
        for i in range(10):
            button = tk.Button(self, text=str(i), font=('Calibri', 16),bd=0)
            button
            numberbuttons.append(button)

        numberbuttons[0].configure(image=self.r0)
        numberbuttons[1].configure(image=self.r1)
        numberbuttons[2].configure(image=self.r2)
        numberbuttons[3].configure(image=self.r3)
        numberbuttons[4].configure(image=self.r4)
        numberbuttons[5].configure(image=self.r5)
        numberbuttons[6].configure(image=self.r6)
        numberbuttons[7].configure(image=self.r7)
        numberbuttons[8].configure(image=self.r8)
        numberbuttons[9].configure(image=self.r9)


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
        period.configure(image=self.rperiod)
        period.place(x=40, y=100, width=30, height=20)

        equal = tk.Button(self, text='=', font=('Calibri', 16),bd=0)
        equal.configure(image=self.requal)
        equal.place(x=70, y=100, width=30, height = 20)

        plus = tk.Button(self, text='+', font=('Calibri', 16),bd=0)
        plus.configure(image=self.rplus)
        plus.place(x=100, y=40, width=30, height=20)

        minus = tk.Button(self, text='-', font=('Calibri', 16),bd=0)
        minus.configure(image=self.rminus)
        minus.place(x=100, y=60, width=30, height=20)

        multiply = tk.Button(self, text='*', font=('Calibri', 16),bd=0)
        multiply.configure(image=self.rmultiply)
        multiply.place(x=100, y=80, width=30, height=20)

        divide = tk.Button(self, text='/', font=('Calibri', 16),bd=0)
        divide.configure(image=self.rdivide)
        divide.place(x=100, y=100, width=30, height=20)

        all_clear = tk.Button(self,text='C', font=('Calibri',16),bd=0)
        all_clear.configure(image=self.rall_clear)
        all_clear.place(x=130, y=40, width=120, height=61)
        all_clear.bind("<Button-1>", self.all_clear_press)
        all_clear.bind("<ButtonRelease-1>", self.all_clear_release)


    def all_clear_press(self, event):
        event.widget.configure(image=self.pall_clear)


    def all_clear_release(self, event):
        event.widget.configure(image=self.rall_clear)




if __name__ == "__main__":
    f = window()
    f.pack()
    f.mainloop()

