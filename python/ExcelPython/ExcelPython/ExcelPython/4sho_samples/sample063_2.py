import openpyxl
fname = '営業所情報04.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.column_dimensions['A'].width = 11
ws.column_dimensions['B'].width = 26
ws.column_dimensions['C'].width = 11
wb.save(fname)
