import openpyxl
fname = '入荷予定06.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws['E9'].value = '=SUM(E4:E8)'
wb.save(fname)
