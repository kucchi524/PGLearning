import openpyxl
fname = 'メンバー情報07.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i in range(4, 8):
    ws.row_dimensions[i].hidden = True
wb.save(fname)
