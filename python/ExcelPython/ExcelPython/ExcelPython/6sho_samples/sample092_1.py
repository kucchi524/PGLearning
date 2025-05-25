import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws['A1'].value = 'サンプル'
wb.save('作成見本.xlsx')
