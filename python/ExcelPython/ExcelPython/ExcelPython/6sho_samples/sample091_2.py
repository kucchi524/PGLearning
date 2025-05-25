import os
import win32com.client
import tkinter
from tkinter import simpledialog
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '店舗別09.xlsx')
root = tkinter.Tk()
root.withdraw()
pdf = simpledialog.askstring('ファイル名',
                             '保存するPDFファイル名を入力してください')
if pdf:
    pfname = os.path.join(pname, pdf + '.pdf')
    xlApp = win32com.client.Dispatch('Excel.Application')
    xlApp.Visible = True
    wb = xlApp.Workbooks.Open(fname)
    wb.ActiveSheet.ExportAsFixedFormat(Type=0,
                                       Filename=pfname)
    xlApp.Quit()
