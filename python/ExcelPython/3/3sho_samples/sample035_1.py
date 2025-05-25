import openpyxl
fname = '入荷予定01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i in range(1, 6):
    ws.cell(i + 3, 1).value = i
wb.save(fname)
