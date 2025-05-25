import openpyxl
fname = '店舗別06.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.worksheets[-1]
wb.move_sheet(ws, offset=-2)
wb.save(fname)
