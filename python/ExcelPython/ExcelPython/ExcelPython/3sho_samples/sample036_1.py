import openpyxl
fname = '入荷予定02.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i in range(1, 6):
    ws.cell(i + 3, 2).value = '商品' + chr(64 + i)
wb.save(fname)
