import openpyxl
fname = '入荷予定06.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i in range(4, 9):
    ws.cell(i, 6).value = f'=D{i}*E{i}'
wb.save(fname)
