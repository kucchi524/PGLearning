import openpyxl
wb = openpyxl.load_workbook('販売記録01.xlsx')
ws = wb.active
print(ws['B4'].value)
