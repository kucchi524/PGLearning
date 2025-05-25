import openpyxl
fname = '注文記録01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws['C8'].value = '海鮮セットC'
wb.save(fname)
