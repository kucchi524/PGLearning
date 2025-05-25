import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import datetime
import os
import win32com.client

def view_data(event=None):
    st_num = ws.Range('在庫[在庫数]').Cells(
        cbox.current() + 1).Value
    snum.set(int(st_num))
    inum.set(1)

def input_data():
    itext = cv.get()
    dtext = rv.get()
    svalue = snum.get()
    ivalue = inum.get()
    if itext == '商品選択':
        mb.showerror('商品未選択', '商品を選択してください')
    elif dtext == '売上' and svalue < ivalue:
        mb.showerror('在庫超過', '在庫数が不足しています')
    elif ivalue < 1:
        mb.showerror('入力値過少', '正の数で入力してください')
    else:
        nr = ws.ListObjects('記録').ListRows.Add().Range
        tday = datetime.date.today().strftime('%Y/%m/%d')
        nr.Cells(1).Value = tday
        nr.Cells(2).Value = itext
        nr.Cells(3).Value = dtext
        if dtext == '売上':
            ivalue = -ivalue
        nr.Cells(4).Value = ivalue
        mb.showinfo('入力完了', '入出庫を記録しました')
        view_data()
    
def close_process():
    wb.Close(SaveChanges=True)
    xlApp.Quit()
    root.destroy()

pname = os.path.dirname(__file__)
fname = os.path.join(pname, '在庫管理.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
ws = wb.ActiveSheet

root = tk.Tk()
root.geometry('260x180')
root.title('入出庫入力')
frame = ttk.Frame(root)
frame.pack()

lbl1 = ttk.Label(frame, text='商品名:')
cv = tk.StringVar(value='商品選択')
i_menu = []
for icel in ws.Range('在庫[商品名]'):
    i_menu.append(icel.Value)
cbox = ttk.Combobox(frame, width=14, textvariable=cv,
                    state='readonly', values=i_menu)
cbox.bind('<<ComboboxSelected>>', view_data)
snum = tk.IntVar()
nlbl1 = ttk.Label(frame, text='現在の在庫数:')
nlbl2 = ttk.Label(frame, textvariable=snum)
dframe = ttk.Labelframe(frame, text='摘要')
rv = tk.StringVar(value='売上')
rb1 = ttk.Radiobutton(dframe, text='売上', value='売上',
                      variable=rv)
rb2 = ttk.Radiobutton(dframe, text='仕入', value='仕入',
                      variable=rv)
lbl3 = ttk.Label(frame, text='数量:')
inum = tk.IntVar(value=1)
ibox = ttk.Entry(frame, width=14, justify='right',
                 textvariable=inum)
btn1 = ttk.Button(frame, width=14, text='入力',
                  command=input_data)
btn2 = ttk.Button(frame, width=14, text='閉じる',
                  command=close_process)

lbl1.grid(row=0, column=0, padx=5, pady=10, sticky='e')
cbox.grid(row=0, column=1, padx=2, pady=10, columnspan=2)
nlbl1.grid(row=1, column=0, padx=5, pady=0, sticky='e')
nlbl2.grid(row=1, column=1, padx=2, pady=0, sticky='w')
dframe.grid(row=2, column=0, padx=0, pady=3, columnspan=2)
rb1.grid(row=0, column=0, padx=25, pady=0)
rb2.grid(row=0, column=1, padx=25, pady=0)
lbl3.grid(row=3, column=0,padx=5, pady=3, sticky='e')
ibox.grid(row=3, column=1, padx=2, pady=0, columnspan=2)
btn1.grid(row=4, column=0, padx=5, pady =8)
btn2.grid(row=4, column=1, padx=5, pady =8)

root.mainloop()
