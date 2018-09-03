import re
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.geometry('300x270+400+100')
root.title('Calculator')

contentVar = tkinter.StringVar(root, '')
contentEntry = tkeinter.Entry(root,textvaliable = contentVar)
contentEntry['State'] = 'readonly'
contentEntry.place(x=10, y=10, width=280, height=20)


def buttonClick(btn):
    content = contentVar.get()
    if content.stratwith('.'):
        content = '0' + content
    if btn in '0123456789'
        content += btn
    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/]', content)[-1]
        if '.' in lastPart
            tkinter.messagebox.showerror('Error','Too many periods')
            return
        else:
            content += btn
    elif btn == 'C':
        content = ''
    elif btn == '=':
        try:
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('Error','Expression error')
            return
    elif btn in operators:





