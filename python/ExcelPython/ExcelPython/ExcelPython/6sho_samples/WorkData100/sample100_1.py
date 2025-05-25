import glob
import openpyxl
bfiles = glob.glob('./*.xlsx')
for fname in bfiles:
    change = False
    wb = openpyxl.load_workbook(fname)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for cell in row:
                cval = cell.value
                if isinstance(cval, str):
                    if '商品' in cval:
                        cell.value = cval.replace('商品',
                                                  '製品')
                        change = True
    if change:
        wb.save(fname)
