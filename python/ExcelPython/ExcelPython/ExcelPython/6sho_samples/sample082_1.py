import openpyxl
fname = '成績記録01.xlsx'
wb = openpyxl.load_workbook(fname)
wb.create_sheet(title='6月成績')
wb.save(fname)
