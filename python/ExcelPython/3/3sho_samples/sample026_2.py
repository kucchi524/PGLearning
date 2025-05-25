import openpyxl
wb = openpyxl.load_workbook('販売記録01.xlsx', data_only=True)
ws = wb.active
print(ws['E4'].value)
