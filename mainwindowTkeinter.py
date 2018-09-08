import tkinter as tk


class Ap_00(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.configure(width=1000,height=480,bg='lightgreen')
        self.master.title('クラスと使ったウィンドウのテスト')
        self.master.resizable(0, 0)  # ウィンドウサイズ変更の禁止
        print(str(self.cget('width')))
        print(str(self.cget('height')))

    def prg_G33c(self):
        print('G33c　tkinter クラスを使ったウィンドウ')
        root = tk.Tk()  # メインウィンドウを作成
        root.title('クラスを使ったウィンドウのテスト')  # メインウィンドウのタイトル設定
        app = Ap_00(master=root)

f=Ap_00()
f.pack()
f.mainloop()