import openpyxl
fname = '店舗別12.xlsx'
wb = openpyxl.load_workbook(fname)
for ws in wb.worksheets:
    ws['B4'].value += 10
wb.save(fname)
