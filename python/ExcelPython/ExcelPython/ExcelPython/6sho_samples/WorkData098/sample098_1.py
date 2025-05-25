import glob
import openpyxl
bfiles = glob.glob('./*.xlsx')
for fname in bfiles:
    wb = openpyxl.load_workbook(fname)
    for ws in wb.worksheets:
        ws['D1'].value = '作業完了'
    wb.save(fname)
