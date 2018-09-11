# -*- coding: utf-8 -*-

import tkinter as tk

class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master,  width=722, height=375)
        self.img = tk.PhotoImage(file='./resource/background.png')
        label = tk.Label(self, image=self.img)
        label.place(x=0, y=0, width=722, height=375)
        self.master.title('Calc')
        self.master.resizable(False, False)

        # Display Contents
        self.contentVar = tk.StringVar(self, '')
        contentEntry = tk.Entry(self, textvariable=self.contentVar, font="Helvetica 36 bold",justify= 'right')
        contentEntry['state'] = 'readonly'
        contentEntry.place(x=211, y=20, width=300, height=70)
        content = "12345.678"
        self.contentVar.set(content)

        # Buttons
        buttons = []
        for i in range(0,17):
            button = tk.Button(self, text=str(i), bd=0)
            buttons.append(button)

        # Binding
        for i in range(17):
            buttons[i].bind("<Button-1>", self.btn_press)
            buttons[i].bind("<ButtonRelease-1>", self.btn_release)

        # Image mapping
        self.press_img = []
        self.release_img = []
        for n in range(0, 17):
            filename = './resource/Press_%d.png' % n
            self.press_img.append(tk.PhotoImage(file=filename))
            filename = './resource/Release_%d.png' % n
            self.release_img.append(tk.PhotoImage(file=filename))
        for n in range(0,17):
            buttons[n].configure(image=self.release_img[n])  # images of released buttons

        # Layout
        buttons[0].place(x=21, y=314, width=120, height=61)
        buttons[1].place(x=21, y=244, width=120, height=61)
        buttons[2].place(x=161, y=244, width=120, height=61)
        buttons[3].place(x=301, y=244, width=120, height=61)
        buttons[4].place(x=21, y=174, width=120, height=61)
        buttons[5].place(x=161, y=174, width=120, height=61)
        buttons[6].place(x=301, y=174, width=120, height=61)
        buttons[7].place(x=21, y=104, width=120, height=61)
        buttons[8].place(x=161, y=104, width=120, height=61)
        buttons[9].place(x=301, y=104, width=120, height=61)
        buttons[10].place(x=161, y=314, width=120, height=61)  # period
        buttons[11].place(x=301, y=314, width=120, height=61)  # equal
        buttons[12].place(x=441, y=314, width=120, height=61)  # plus
        buttons[13].place(x=441, y=104, width=120, height=61)  # minus
        buttons[14].place(x=441, y=174, width=120, height=61)  # multiply
        buttons[15].place(x=441, y=244, width=120, height=61)  # divide
        buttons[16].place(x=581, y=104, width=120, height=61)  # all_clear


        self.wait_initial_input = True
        self.work = 0
        self.operation = ""


    def btn_press(self, event):
        btn = event.widget["text"]
        event.widget.configure(image=self.press_img[int(btn)])  # images of pressed buttons
        list01 = ("0","1","2","3","4","5","6","7","8","9")
        if btn in list01:
            print(btn)
            self.digit_entry(btn)
        elif btn == '10':
            print('period button')
            self.period_entry()
        elif btn == '11':
            print('equal button')
            self.operator_entry("=")
        elif btn == '12':
            print('plus button')
            self.operator_entry("+")
        elif btn == '13':
            print('minus button')
            self.operator_entry("-")
        elif btn == '14':
            print('multiply button')
            self.operator_entry("*")
        elif btn == '15':
            print('divide button')
            self.operator_entry("/")
        elif btn == '16':
            print('all clear button')
            self.ac_entry()
        else:
            print('other buttons')

    def btn_release(self, event):
        event.widget.configure(image=self.release_img[int(event.widget["text"])])



    # Calculator
    def digit_entry(self, btn):
        if self.wait_initial_input:  # 初回キー入力待ち
            print("inital")
            print(self.work)
            contents = btn
            self.contentVar.set(contents)
            self.wait_initial_input = False
        else:
            if self.contentVar.get() == "0":
                contents = btn
            else:
                contents = self.contentVar.get() + btn
        self.contentVar.set(contents)

    def period_entry(self):
        if self.wait_initial_input:
            contents = "0."
            self.wait_initial_input = False
        elif '.' not in (self.contentVar.get()):  # 小数点の複数回入力抑止
            contents = self.contentVar.get() + "."
        self.contentVar.set(contents)

    def operator_entry(self, btn):
        #btn = event.widget['text']
        print(btn + 'was operated')
        if btn == '+':
            if not self.wait_initial_input:  # 演算子の押しなおしでない
                self.calculate()
            self.work = float(self.contentVar.get())
            self.wait_initial_input = True
            print(self.operation)
            print("work is " + str(self.work))
            self.operation = '+'
        elif btn == '-':
            if not self.wait_initial_input:  # 演算子の押しなおしでない
                self.calculate()
            self.work = float(self.contentVar.get())
            self.wait_initial_input = True
            self.operation = '-'
        elif btn == '*':
            if not self.wait_initial_input:  # 演算子の押しなおしでない
                self.calculate()
            self.work = float(self.contentVar.get())
            self.wait_initial_input = True
            self.operation = '*'
        elif btn == '/':
            if not self.wait_initial_input:  # 演算子の押しなおしでない
                self.calculate()
            self.work = float(self.contentVar.get())
            self.wait_initial_input = True
            self.operation = '/'
        elif btn == '=':
            #self.work = float(self.contentVar.get())
            print(" = was pressed")
            print(" work is " + str(self.work))
            print(" operator is " + self.operation)
            self.wait_initial_input = True
            print("operation = " + self.operation)
            self.calculate()
            self.operation = ""

    def calculate(self):
        contents = float(self.contentVar.get())
        if self.operation == '+':
            contents = self.work + contents
        elif self.operation == '-':
            contents = self.work - contents
        elif self.operation == '*':
            contents = self.work * contents
        elif self.operation == '/':
            if contents == 0:
                pass
            else:
                contents = self.work / contents

        contents = round(contents, 8)  # 小数点以下 8 桁までに丸める

        d = str(contents).rsplit('.', 1)  # 小数点の右側
        if float(d[1]) == 0:  # ゼロの場合
            contents = d[0]   # ゼロの左側のみを採用

        if len(d[0]) > 10:  # 整数部分が　10 桁を超えるとエラー
            contents = "error"
        self.contentVar.set(contents)
        self.wait_initial_input = True


    def ac_entry(self):
        self.operation = ''
        self.work = 0
        self.contentVar.set('0')
        self.wait_initial_input == True

#    def display_error(self):
#        self.contentVar.set(100000)

if __name__ == "__main__":
    f = window()
    f.pack()
    f.mainloop()

