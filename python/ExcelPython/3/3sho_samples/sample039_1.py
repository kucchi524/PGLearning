import openpyxl
fname = 'メンバー情報01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws.iter_rows(min_row=4):
    row[4].value += '班'
wb.save(fname)
