import openpyxl
from openpyxl.styles import Font
fname = '注文記録04.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
fnt = Font(color='0000FF', bold=True)
for cel in ws['A3:E3'][0]:
    cel.font = fnt
wb.save(fname)
