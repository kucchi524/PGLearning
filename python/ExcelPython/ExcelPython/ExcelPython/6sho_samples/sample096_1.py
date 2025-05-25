import openpyxl
fname = '店舗別12.xlsx'
wb = openpyxl.load_workbook(fname)
for ws in wb.worksheets:
    ws['A1'].value = ws.title
wb.save(fname)
