import tkinter
from tkinter import filedialog as fd
import glob
import os
import openpyxl
root = tkinter.Tk()
root.withdraw()
fpath = fd.askdirectory(initialdir=os.path.abspath('.'))
if fpath:
    sname = fd.asksaveasfilename(initialfile='ブック一覧.xlsx',
                                 filetypes=[('Excelブック', '*.xlsx')])
    if sname:
        if sname[-5:] != '.xlsx':
            sname += '.xlsx'
        wb = openpyxl.Workbook()
        ws = wb.active
        ws['A1'].value = fpath
        bfiles = glob.glob(fpath + "/*.xls[xm]")
        for i, pname in enumerate(bfiles):
            fname = os.path.basename(pname)
            line = [i + 1, fname]
            ws.append(line)
        wb.save(sname)
