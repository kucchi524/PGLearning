import openpyxl
fname = '成績記録01.xlsx'
wb = openpyxl.load_workbook(fname)
wb.create_sheet(title='5月成績', index=1)
wb.save(fname)
