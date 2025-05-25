import openpyxl
from openpyxl.styles.numbers import builtin_format_code
fname = '注文記録06.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws.iter_rows(min_row=4):
    row[3].number_format = builtin_format_code(6)
wb.save(fname)
