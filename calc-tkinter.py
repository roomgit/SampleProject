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

        # Display Contents
        self.contentVar = tk.StringVar(self,'')
        contentEntry = tk.Entry(self, textvariable=self.contentVar)
        contentEntry['state'] = 'readonly'
        contentEntry.place(x=250, y=30, width=300, height=60)
        content = "12345.678"
        self.contentVar.set(content)

        # Image file reading
        self.pimg=[]
        self.rimg=[]
        for n in range (0,10):
            filename='./resource/Press_%d.png' % (n)
            self.pimg.append(tk.PhotoImage(file=filename))
            filename = './resource/Release_%d.png' % (n)
            self.rimg.append(tk.PhotoImage(file=filename))

        self.pperiod = tk.PhotoImage(file='./resource/Press_period.png')
        self.pequal = tk.PhotoImage(file='./resource/Press_equal.png')
        self.pplus = tk.PhotoImage(file='./resource/Press_plus.png')
        self.pminus = tk.PhotoImage(file='./resource/Press_minus.png')
        self.pmultiply = tk.PhotoImage(file='./resource/Press_multiply.png')
        self.pdivide = tk.PhotoImage(file='./resource/Press_divide.png')
        self.pall_clear = tk.PhotoImage(file='./resource/Press_AC.png')
        self.rperiod = tk.PhotoImage(file='./resource/Release_period.png')
        self.requal = tk.PhotoImage(file='./resource/Release_equal.png')
        self.rplus = tk.PhotoImage(file='./resource/Release_plus.png')
        self.rminus = tk.PhotoImage(file='./resource/Release_minus.png')
        self.rmultiply = tk.PhotoImage(file='./resource/Release_multiply.png')
        self.rdivide = tk.PhotoImage(file='./resource/Release_divide.png')
        self.rall_clear = tk.PhotoImage(file='./resource/Release_AC.png')

        numberbuttons = []
        for i in range(0,10):
            button = tk.Button(self, text=str(i), bd=0)
            numberbuttons.append(button)

        for n in range(0,10):
            numberbuttons[n].configure(image=self.rimg[n])

        period = tk.Button(self, text='.', bd=0, image=self.rperiod)
        equal = tk.Button(self, text='=', bd=0,image=self.requal)
        plus = tk.Button(self, text='+', bd=0, image=self.rplus)
        minus = tk.Button(self, text='-', bd=0, image=self.rminus)
        multiply = tk.Button(self, text='*', bd=0, image=self.rmultiply)
        divide = tk.Button(self, text='/', bd=0,image=self.rdivide)
        all_clear = tk.Button(self, text='C', bd=0, image=self.rall_clear)

        # Binding
        for i in range(10):
            numberbuttons[i].bind("<Button-1>", self.btn_press)
            numberbuttons[i].bind("<ButtonRelease-1>", self.btn_release)
        period.bind("<Button-1>", self.period_press)
        period.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.rperiod))
        equal.bind("<Button-1>", self.operator_press)
        equal.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.requal))
        plus.bind("<Button-1>", self.operator_press)
        plus.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.rplus))
        minus.bind("<Button-1>", self.operator_press)
        minus.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.rminus))
        multiply.bind("<Button-1>", self.operator_press)
        multiply.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.rmultiply))
        divide.bind("<Button-1>", self.operator_press)
        divide.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.rdivide))
        all_clear.bind("<Button-1>", self.all_clear_press)
        all_clear.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.rall_clear))

        # Layout
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
        period.place(x=40, y=100, width=30, height=20)
        equal.place(x=70, y=100, width=30, height = 20)
        plus.place(x=100, y=40, width=30, height=20)
        minus.place(x=100, y=60, width=30, height=20)
        multiply.place(x=100, y=80, width=30, height=20)
        divide.place(x=100, y=100, width=30, height=20)
        all_clear.place(x=130, y=40, width=120, height=61)

        self.wait_initial_input = True
        self.work = 0
        self.operation = ""

    def btn_press(self, event):
        btn = event.widget["text"]
        event.widget.configure(image=self.pimg[int(btn)])
        if self.wait_initial_input == True:
            self.work = float(self.contentVar.get())
            print("inital")
            print(self.work)
            contents = btn
            self.contentVar.set(contents)
            self.wait_initial_input == False

        self.contentVar.set(btn)

    def period_press(self,event):
        btn = event.widget['text']
        print(btn)
        event.widget.configure(image=self.pperiod)

    def operator_press(self,event):
        btn = event.widget['text']
        print(btn)
        if btn == '+':
            event.widget.configure(image=self.pplus)
            self.wait_initial_input = True
            self.operation = '+'
        elif btn == '-':
            event.widget.configure(image=self.pminus)
            self.wait_initial_input = True
            self.operation = '-'
        elif btn == '*':
            event.widget.configure(image=self.pmultiply)
            self.wait_initial_input = True
            self.operation = '*'
        elif btn == '/':
            event.widget.configure(image=self.pdivide)
            self.wait_initial_input = True
            self.operation = '/'
        elif btn == '=':
            event.widget.configure(image=self.pequal)
            if self.operation == '+':
                contents = + self.work + int(self.contentVar.get())
            elif self.operation == '-':
                contents = self.work - int(self.contentVar.get())
            elif self.operation == '*':
                contents = self.work * int(self.contentVar.get())
            elif self.operation == '/':
                contents = self.work / int(self.contentVar.get())
            else:
                pass
            self.contentVar.set(contents)

            self.wait_initial_input = True
            self.operation = ''
            work = 0

    def btn_release(self, event):
        event.widget.configure(image=self.rimg[int(event.widget["text"])])

    def all_clear_press(self, event):
        event.widget.configure(image=self.pall_clear)
        self.saved_operator='None'
        self.work=0
        self.contentVar.set('0')







if __name__ == "__main__":
    f = window()
    f.pack()
    f.mainloop()

