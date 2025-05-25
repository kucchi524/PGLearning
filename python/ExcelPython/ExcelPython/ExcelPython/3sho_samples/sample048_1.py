import openpyxl
fname = '成績表01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.move_range('A2:E7', rows=2, cols=1, translate=True)
wb.save(fname)
