import tkinter
from tkinter import simpledialog, messagebox
root = tkinter.Tk()
root.withdraw()
ninzu = simpledialog.askstring('人数',
                               '予約人数を入力してください\n'
                               '（未定の場合は「未定」と入力）')
if ninzu:
    if ninzu == '未定':
        messagebox.showwarning('人数未定',
                               '人数が決まったらお知らせください')
    else:
        try:
            ryokin = int(ninzu) * 1000
            messagebox.showinfo('料金',
                                f'利用料金は{ryokin}円です')
        except:
            messagebox.showerror('エラー', '入力値が不適切です')
