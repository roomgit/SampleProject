# -*- coding: utf-8 -*-

import tkinter as tk

# For pyinstaller
def resource_path(relative):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, relative)
  return os.path.join(relative)


class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master,  width=722, height=375)
        self.master.title('Calc-10')
        self.master.resizable(False, False)
        self.img = tk.PhotoImage(file=resource_path("./resource/background.png"))
        label = tk.Label(self, image=self.img)
        label.place(x=0, y=0, width=722, height=375)

        # Display Contents
        self.contentVar = tk.StringVar(self, '')
        contentEntry = tk.Entry(self, textvariable=self.contentVar, font="Helvetica 36 bold ", justify='right')
        contentEntry['state'] = 'readonly'
        contentEntry.place(x=211, y=20, width=300, height=70)
        content = "0"
        self.contentVar.set(content)

        # Error icon
        self.err_icon = tk.Label(self, font="Helvetica 10", text='')
        self.err_icon.place(x=213, y=24, width=10, height=10)

        # Buttons
        buttons = []
        for i in range(0, 18):
            button = tk.Button(self, text=str(i), bd=0)
            buttons.append(button)

        # Binding
        for i in range(0, 18):
            buttons[i].bind("<Button-1>", self.btn_press)
            buttons[i].bind("<ButtonRelease-1>", self.btn_release)

        # Image mapping
        self.press_img = []
        self.release_img = []
        for n in range(0, 18):
            filename = resource_path("./resource/Press_%d.png") % n
            self.press_img.append(tk.PhotoImage(file=filename))
            filename = resource_path("./resource/Release_%d.png") % n
            self.release_img.append(tk.PhotoImage(file=filename))
        for n in range(0, 18):
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
        buttons[13].place(x=441, y=244, width=120, height=61)  # minus
        buttons[14].place(x=441, y=174, width=120, height=61)  # multiply
        buttons[15].place(x=441, y=104, width=120, height=61)  # divide
        buttons[16].place(x=581, y=104, width=120, height=61)  # all_clear
        buttons[17].place(x=581, y=174, width=120, height=61)  # all_clear

        self.wait_initial_input = True
        self.work = 0
        self.operation = ""

    def btn_press(self, event):
        btn = event.widget["text"]
        event.widget.configure(image=self.press_img[int(btn)])  # images of pressed buttons
        list0 = ("0","1","2","3","4","5","6","7","8","9")
        if btn in list0:
            self.digit_entry(btn)
        elif btn == '10':
            self.period_entry()
        elif btn == '11':
            self.equal_entry()
        elif btn in '12':
            self.operator_entry("+")
        elif btn == '13':
            self.operator_entry("-")
        elif btn == '14':
            self.operator_entry("*")
        elif btn == '15':
            self.operator_entry("/")
        elif btn == '16':
            self.ac_entry()
        elif btn == '17':
            self.c_entry()


    def btn_release(self, event):
        event.widget.configure(image=self.release_img[int(event.widget["text"])])

    #
    # Calculator
    #
    def digit_entry(self, btn):
        self.err_icon.configure(text="")
        if len(self.contentVar.get()) >= 10:  # limit input up to 10 digits
            return
        if self.wait_initial_input:  # Waiting the first digit key input
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
        self.err_icon.configure(text="")
        if self.wait_initial_input:
            self.contentVar.set("0.")
            self.wait_initial_input = False
        elif '.' not in (self.contentVar.get()):  # Inhibits multiple periods
            contents = self.contentVar.get() + "."
            self.contentVar.set(contents)

    def operator_entry(self, btn):
        if not self.wait_initial_input:  # Not a repeated operator button press
            self.calculate()
        self.work = float(self.contentVar.get())
        self.wait_initial_input = True
        self.operation = btn

    def equal_entry(self):
        self.calculate()
        self.wait_initial_input = True
        self.operation = ""

    def ac_entry(self):
        self.err_icon.configure(text="")
        self.operation = ''
        self.work = 0
        self.contentVar.set('0')
        self.wait_initial_input = True

    def c_entry(self):
        self.contentVar.set('0')

    def calculate(self):
        value = float(self.contentVar.get())
        if self.operation == '+':
            value = self.work + value
        elif self.operation == '-':
            value = self.work - value
        elif self.operation == '*':
            value = self.work * value
        elif self.operation == '/':
            if value == 0:
                self.err_icon.configure(text="E")
            else:
                value = self.work / value

        # Formatting
        if value.is_integer():
            if value > 9999999999:  # Exceeds 10 digits?
                self.err_icon.configure(text="E")
                contents = "0"
            else:
                contents = str(int(value))  # Remove zeros after period
        else:
            contents = "%.10f" % value  # Converts to fixed-point format
            d = contents.rsplit('.', 1)  # Divide by period
            if len(d[0]) > 10:  # Integer portion exceeds 10 digits
                self.err_icon.configure(text="E")
                contents = "0"
            else:
                value = float(value)
                place = 9 - len(d[0])  # determine how many digits after the period can be displayed
                contents = str(round(value, place))

        self.contentVar.set(contents)




#    def display_error(self):
#        self.contentVar.set(100000)


if __name__ == "__main__":
    f = window()
    f.pack()
    f.mainloop()

