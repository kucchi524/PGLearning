import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.withdraw()
if messagebox.askyesno('得点','50点以上ですか？'):
    messagebox.showinfo('判定', '合格です')
