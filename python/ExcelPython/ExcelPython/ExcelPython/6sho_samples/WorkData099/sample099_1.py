import glob
import os
import openpyxl
bfiles = glob.glob('./*.xlsx')
for fname in bfiles:
    wb = openpyxl.load_workbook(fname)
    bname = os.path.basename(fname)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                if cell.value == '商品B':
                    print(bname, ws.title, cell.coordinate)
