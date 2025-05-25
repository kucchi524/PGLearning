import openpyxl
fname = 'メンバー情報07.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.row_dimensions[4].hidden = True
wb.save(fname)
