import openpyxl
fname = '営業所情報04.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i, row in enumerate(ws.iter_rows()):
    ws.row_dimensions[i + 1].height = 24
wb.save(fname)
