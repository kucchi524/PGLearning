import openpyxl
fname = 'メンバー情報01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws.iter_rows(min_row=4):
    num = format(row[0].value,'0>4')
    row[0].value = 'P' + num + 'TS'
wb.save(fname)
