# -*- coding:utf-8 -*-
import tkinter as tk
root = tk.Tk()

# ウィジェットがクリックされたときのイベントを定義
def callback(event):
    print(event.widget["text"])

for i in range(5):
    # ボタンの定義
    button = tk.Button(root,text="ボタン"+str(i))
    # ウィジェットが左クリックされたときの関数を定義
    button.bind("<1>",callback)
    # ボタンの配置
    button.pack(fill="x")

root.mainloop()