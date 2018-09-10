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
        self.press_img=[]
        self.release_img=[]
        for n in range (0,17):
            filename='./resource/Press_%d.png' % (n)
            self.press_img.append(tk.PhotoImage(file=filename))
            filename = './resource/Release_%d.png' % (n)
            self.release_img.append(tk.PhotoImage(file=filename))

        buttons = []
        for i in range(0,17):
            button = tk.Button(self, text=str(i), bd=0)
            buttons.append(button)

        for n in range(0,17):
            buttons[n].configure(image=self.release_img[n])

        #period = tk.Button(self, text='.', bd=0, image=self.release_img[10])
        #buttons[10].configure(text='.')
        #equal = tk.Button(self, text='=', bd=0,image=self.release_img[11])
        #buttons[11].configure(text='=')
        #plus = tk.Button(self, text='+', bd=0, image=self.release_img[12])
        #buttons[12].configure(text='+')
        #minus = tk.Button(self, text='-', bd=0, image=self.release_img[13])
        #buttons[13].configure(text='-')
        #multiply = tk.Button(self, text='*', bd=0, image=self.release_img[14])
        #buttons[14].configure(text='*')
        #divide = tk.Button(self, text='/', bd=0,image=self.release_img[15])
        #buttons[15].configure(text='/')
        #all_clear = tk.Button(self, text='C', bd=0, image=self.release_img[16])
        #buttons[16].configure(text='C')

        # Binding
        for i in range(17):
            buttons[i].bind("<Button-1>", self.btn_press)
            buttons[i].bind("<ButtonRelease-1>", self.btn_release)
        #period.bind("<Button-1>", self.period_press)
        #period.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.release_img[10]))
        #equal.bind("<Button-1>", self.operator_press)
        #equal.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.release_img[11]))
        #plus.bind("<Button-1>", self.operator_press)
        #plus.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.release_img[12]))
        #minus.bind("<Button-1>", self.operator_press)
        #minus.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.release_img[13]))
        #multiply.bind("<Button-1>", self.operator_press)
        #multiply.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.release_img[14]))
        #divide.bind("<Button-1>", self.operator_press)
        #divide.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.release_img[15]))
        #all_clear.bind("<Button-1>", self.all_clear_press)
        #all_clear.bind("<ButtonRelease-1>", lambda event: event.widget.configure(image=self.release_img[16]))

        # Layout
        buttons[0].place(x=10, y=100, width=30, height=20)
        buttons[1].place(x=10, y=80, width=30, height=20)
        buttons[2].place(x=40, y=80, width=30, height=20)
        buttons[3].place(x=70, y=80, width=30, height=20)
        buttons[4].place(x=10, y=60, width=30, height=20)
        buttons[5].place(x=40, y=60, width=30, height=20)
        buttons[6].place(x=70, y=60, width=30, height=20)
        buttons[7].place(x=10, y=40, width=30, height=20)
        buttons[8].place(x=40, y=40, width=30, height=20)
        buttons[9].place(x=70, y=40, width=30, height=20)
        buttons[10].place(x=40, y=100, width=30, height=20)  # period
        buttons[11].place(x=70, y=100, width=30, height=20)  # equal
        buttons[12].place(x=100, y=40, width=30, height=20)  # plus
        buttons[13].place(x=100, y=60, width=30, height=20)  # minus
        buttons[14].place(x=100, y=80, width=30, height=20)  # multiply
        buttons[15].place(x=100, y=100, width=30, height=20)  # divide
        buttons[16].place(x=130, y=40, width=120, height=61)  # all_clear
        #period.place(x=40, y=100, width=30, height=20)
        #equal.place(x=70, y=100, width=30, height = 20)
        #plus.place(x=100, y=40, width=30, height=20)
        #minus.place(x=100, y=60, width=30, height=20)
        #multiply.place(x=100, y=80, width=30, height=20)
        #divide.place(x=100, y=100, width=30, height=20)
        #all_clear.place(x=130, y=40, width=120, height=61)

        self.wait_initial_input = True
        self.work = 0
        self.operation = ""


    def calculate(self,btn):
        print(btn + 'was operated')

        if btn == '+':
            #event.widget.configure(image=self.press_img[12])
            self.wait_initial_input = True
            self.operation = '+'
        elif btn == '-':
            #event.widget.configure(image=self.press_img[13])
            self.wait_initial_input = True
            self.operation = '-'
        elif btn == '*':
            #event.widget.configure(image=self.press_img[14])
            self.wait_initial_input = True
            self.operation = '*'
        elif btn == '/':
            #event.widget.configure(image=self.press_img[15])
            self.wait_initial_input = True
            self.operation = '/'
        elif btn == '=':
            #event.widget.configure(image=self.press_img[10])
            if self.operation == '+':
                contents = self.work + float(self.contentVar.get())
            elif self.operation == '-':
                contents = self.work - float(self.contentVar.get())
            elif self.operation == '*':
                contents = self.work * float(self.contentVar.get())
            elif self.operation == '/':
                contents = self.work / float(self.contentVar.get())
            else:
                contents = float(self.contentVar.get())

            self.contentVar.set(contents)
            self.wait_initial_input = True
            self.operation = ''
            self.work = 0

    def btn_press(self, event):
        btn = event.widget["text"]
        event.widget.configure(image=self.press_img[int(btn)])
        list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        if btn in list:
            print(btn)

            if self.wait_initial_input == True:
                self.work = float(self.contentVar.get())
                print("inital")
                print(self.work)
                contents = btn
                self.contentVar.set(contents)
                self.wait_initial_input = False
            else:
                self.work = float(self.contentVar.get())
                contents= self.contentVar.get() + btn

            self.contentVar.set(contents)

        elif btn == '+':
           print('plus button')
        elif btn == '-':
           print('minus button')
        elif btn == '*':
           print('multiply button')
        elif btn == '/':
           print(' divide button')
        elif btn == '=':
           print('equal button')
        elif btn == 'C':
           print('all clear button')
        else:
            print('other buttons')

    def button_release(self,event):
        btn = event.widget["text"]
        event.widget.configure(image=self.release_img[int(btn)])


    def period_press(self,event):
        btn = event.widget['text']
        print(btn)
        event.widget.configure(image=self.press_img[10])

    def operator_press(self,event):
        b = event.widget['text']
        #print(btn)

        self.calculate(b)

        '''
        if btn == '+':
            event.widget.configure(image=self.press_img[12])
            self.wait_initial_input = True
            self.operation = '+'
        elif btn == '-':
            event.widget.configure(image=self.press_img[13])
            self.wait_initial_input = True
            self.operation = '-'
        elif btn == '*':
            event.widget.configure(image=self.press_img[14])
            self.wait_initial_input = True
            self.operation = '*'
        elif btn == '/':
            event.widget.configure(image=self.press_img[15])
            self.wait_initial_input = True
            self.operation = '/'
        elif btn == '=':
            event.widget.configure(image=self.press_img[10])
            if self.operation == '+':
                contents = self.work + float(self.contentVar.get())
            elif self.operation == '-':
                contents = self.work - float(self.contentVar.get())
            elif self.operation == '*':
                contents = self.work * float(self.contentVar.get())
            elif self.operation == '/':
                contents = self.work / float(self.contentVar.get())
            else:
                contents = float(self.contentVar.get())

            self.contentVar.set(contents)
            self.wait_initial_input = True
            self.operation = ''
            self.work = 0
        '''

    def btn_release(self, event):
        event.widget.configure(image=self.release_img[int(event.widget["text"])])

    def all_clear_press(self, event):
        event.widget.configure(image=self.press_img[16])
        self.saved_operator='None'
        self.work=0
        self.contentVar.set('0')







if __name__ == "__main__":
    f = window()
    f.pack()
    f.mainloop()

