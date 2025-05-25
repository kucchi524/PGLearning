import glob
import openpyxl
bfiles = glob.glob('./*.xlsx')
for fname in bfiles:
    wb = openpyxl.load_workbook(fname)
    ws = wb.active
    ws['D1'].value = '作業中'
    wb.save(fname)
