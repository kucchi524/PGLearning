import tkinter
from tkinter import simpledialog, messagebox
root = tkinter.Tk()
root.withdraw()
kosu = simpledialog.askinteger('購入数',
                               '購入したい個数を入力してください')
if kosu:
    kingaku = kosu * 120
    messagebox.showinfo('金額', f'購入金額：{kingaku}円')
