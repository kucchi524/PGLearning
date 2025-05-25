import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import datetime
import os
import win32com.client

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry('260x180')
        self.master.title('入出庫入力')
        self.frame = ttk.Frame(self.master)
        
        self.lbl1 = ttk.Label(self.frame, text='商品名:')
        self.cv = tk.StringVar(value='商品選択')
        self.i_menu = []
        for icel in ws.Range('在庫[商品名]'):
            self.i_menu.append(icel.Value)
        self.cbox = ttk.Combobox(self.frame, width=14, textvariable=self.cv,
                                 state='readonly', values=self.i_menu)
        self.cbox.bind('<<ComboboxSelected>>', view_data)
        self.snum = tk.IntVar()
        self.nlbl1 = ttk.Label(self.frame, text='現在の在庫数:')
        self.nlbl2 = ttk.Label(self.frame, textvariable=self.snum)
        self.dframe = ttk.Labelframe(self.frame, text='摘要')
        self.rv = tk.StringVar(value='売上')
        self.rb1 = ttk.Radiobutton(self.dframe, text='売上', value='売上',
                                   variable=self.rv)
        self.rb2 = ttk.Radiobutton(self.dframe, text='仕入', value='仕入',
                                   variable=self.rv)
        self.lbl3 = ttk.Label(self.frame, text='数量:')
        self.inum = tk.IntVar(value=1)
        self.ibox = ttk.Entry(self.frame, width=14, justify='right',
                              textvariable=self.inum)
        self.btn1 = ttk.Button(self.frame, width=14, text='入力',
                               command=input_data)
        self.btn2 = ttk.Button(self.frame, width=14, text='閉じる',
                               command=close_process)

        self.lbl1.grid(row=0, column=0, padx=5, pady=10, sticky='e')
        self.cbox.grid(row=0, column=1, padx=2, pady=10, columnspan=2)
        self.nlbl1.grid(row=1, column=0, padx=5, pady=0, sticky='e')
        self.nlbl2.grid(row=1, column=1, padx=2, pady=0, sticky='w')
        self.dframe.grid(row=2, column=0, padx=0, pady=3, columnspan=2)
        self.rb1.grid(row=0, column=0, padx=25, pady=0)
        self.rb2.grid(row=0, column=1, padx=25, pady=0)
        self.lbl3.grid(row=3, column=0,padx=5, pady=3, sticky='e')
        self.ibox.grid(row=3, column=1, padx=2, pady=0, columnspan=2)
        self.btn1.grid(row=4, column=0, padx=5, pady =8)
        self.btn2.grid(row=4, column=1, padx=5, pady =8)

        self.frame.pack()
    
    def view_data(event=None):
        st_num = ws.Range('在庫[在庫数]').Cells(cbox.current() +
                                                1).Value
        self.snum.set(int(st_num))
        self.inum.set(1)

    def input_data():
        itext = self.cv.get()
        dtext = self.rv.get()
        svalue = self.snum.get()
        ivalue = self.inum.get()
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
        self.master.destroy()

def main():
    pname = os.path.dirname(__file__)
    fname = os.path.join(pname, '在庫管理.xlsx')
    xlApp = win32com.client.Dispatch('Excel.Application')
    wb = xlApp.Workbooks.Open(fname)
    ws = wb.ActiveSheet
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
