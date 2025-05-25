import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import openpyxl
root = tkinter.Tk()
root.withdraw()
ftype = [('Excelブック', '*.xlsx *.xlsm')]
fname = fd.askopenfilename(filetypes=ftype)
if fname:
    wb = openpyxl.load_workbook(fname)
    ws = wb.active
    total = 0
    ncount = 0
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, (int, float)):
                ncount += 1
                total += cell.value
    mb.showinfo('アクティブシートの情報',
                f'シート名：{ws.title}\n'
                f'数値セルの数：{ncount}\n'
                f'数値セルの合計：{total}')
