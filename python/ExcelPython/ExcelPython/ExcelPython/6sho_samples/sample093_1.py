import openpyxl
wb = openpyxl.load_workbook('作成見本.xlsx')
wb.save('変更見本.xlsx')
