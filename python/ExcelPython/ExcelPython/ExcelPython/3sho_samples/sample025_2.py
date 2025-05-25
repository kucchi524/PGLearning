import openpyxl
wb = openpyxl.load_workbook('販売記録01.xlsx')
ws = wb.active
print(ws.cell(row=5, column=3).value)
