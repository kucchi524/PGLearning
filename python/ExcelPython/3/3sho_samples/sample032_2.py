import openpyxl
fname = '注文記録01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.cell(row=8, column=5).value += 2
wb.save(fname)
