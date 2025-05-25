import openpyxl
fname = '店舗別06.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb['販売数2月']
wb.move_sheet(ws, offset=1)
wb.save(fname)
