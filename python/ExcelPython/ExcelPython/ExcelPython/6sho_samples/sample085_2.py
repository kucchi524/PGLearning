import openpyxl
fname = '店舗別05.xlsx'
wb = openpyxl.load_workbook(fname)
for ws in wb.worksheets:
    if ws.title[:5] == 'Sheet':
        wb.remove(ws)
wb.save(fname)
