import re
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.geometry('300x270+400+100')
root.resizable(False,False)
root.title('Calculator')

contentVar = tkinter.StringVar(root, '')
contentEntry = tkinter.Entry(root,textvariable = contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=10, y=10, width=100, height=20)

contentVar2 = tkinter.StringVar(root, '')
contentEntry2 = tkinter.Entry(root,textvariable = contentVar2)
contentEntry2['state'] = 'readonly'
contentEntry2.place(x=100, y=10, width=90, height=20)

contentVar3 = tkinter.StringVar(root, '')
contentEntry3 = tkinter.Entry(root,textvariable = contentVar3)
contentEntry3['state'] = 'readonly'
contentEntry3.place(x=190, y=10, width=90, height=20)

def buttonClick(btn):
    content = contentVar.get()
    content2 =contentVar2.get()
    content3 =contentVar3.get()

    if content.startswith('.'):
        content = '0' + content
    if content2.startswith('.'):
        content2 = '0' + content2

    if btn in '0123456789':
        if content.endswith('+'):
            content2 = btn
        elif content2 == '0':
            content2 = btn
        else:
            content2 += btn                                                     # Content2
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/]', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('Error','Too many periods')
            return
        else:
            content += btn

        lastPart2 = re.split(r'\+|-|\*|/]', content2)[-1]
        if '.' in lastPart2:
            tkinter.messagebox.showerror('Error','Too many periods in content 2')
            return
        else:
            content2 += btn
    elif btn == 'C':
        content = ''
        content2 = ''
        content3 = ''
    elif btn == '=':
        try:
            content = str(eval(content))   #　Execute Calculation
        except:
            tkinter.messagebox.showerror('Error','Expression error')
            return
    elif btn in operators:
        if content.endswith(operators):
            tkinter.messagebox.showerror('Error', 'Multiple Operators' )
            return
        content += btn

        if content2.endswith(operators):
            tkinter.messagebox.showerror('Error', 'Multiple Operators in 2' )
            return

        content3 = content2


    '''
    elif btn == 'Sqrt':
        n = content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            content = eval(content) ** 0.5
        else:
            tkinter.messagebox.showerror('Error', 'Expression Error')
            return
    '''

    contentVar.set(content)
    contentVar2.set(content2)
    contentVar3.set(content3)
#---------------

btnClear = tkinter.Button(root, text="Clear", command=lambda:buttonClick('C'))
btnClear.place(x=40, y=40, width=80, height=20)
btnCompute = tkinter.Button(root, text='=', command=lambda:buttonClick('='))
btnCompute.place(x=170, y=40, width=80, height=20)

digits = list('0123456789.')+['Sqrt']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit = tkinter.Button(root, text = d, command=lambda x=d:buttonClick(x))
        btnDigit.place(x=20+col*70, y=80+row*50, width=50, height=20)

operators = ('+','-','*','/','**','//')
for index, operator in enumerate(operators):
    btnOperator = tkinter.Button(root,text=operator, command=lambda x=operator:buttonClick(x))
    btnOperator.place(x=230, y=80+index*30, width=50, height=20)


root.mainloop()






