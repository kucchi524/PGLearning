import openpyxl
import glob
import os
wb = openpyxl.Workbook()
ws = wb.active
fpath = os.path.abspath('.')
ws['A1'].value = fpath
bfiles = glob.glob('./*')
for i, pname in enumerate(bfiles):
    fname = os.path.basename(pname)
    line = [i + 1, fname]
    ws.append(line)
wb.save('ファイル一覧.xlsx')
