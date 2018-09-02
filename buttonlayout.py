
# 0 - 9 までのボタンを配置する　(gridを使用）
# ボタンが押されたら、押された番号をprint

import tkinter as tk

class window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        buttons =[]
        for i in range(0,10):
            button = tk.Button(self, text=str(i), font=('Helvetica', '16'), command=lambda num=i: get_variables(num))
            buttons.append(button)

        buttons[1].grid(row=2, column=0)
        buttons[2].grid(row=2, column=1)
        buttons[3].grid(row=2, column=2)
        buttons[4].grid(row=3, column=0)
        buttons[5].grid(row=3, column=1)
        buttons[6].grid(row=3, column=2)
        buttons[7].grid(row=4, column=0)
        buttons[8].grid(row=4, column=1)
        buttons[9].grid(row=4, column=2)
        buttons[0].grid(row=5, column=0)

def get_variables(num):
        print(num)

if __name__ == "__main__":
    f = window()
    f.pack()
    f.mainloop()