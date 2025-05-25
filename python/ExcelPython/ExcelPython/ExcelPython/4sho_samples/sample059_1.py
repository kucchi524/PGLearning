import openpyxl
from openpyxl.styles.borders import Border, Side
fname = '注文記録07.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
sd1 = Side(style='medium', color='00008B')
sd2 = Side(style='thin', color='0000FF')
for i, row in enumerate(ws.iter_rows(min_row=3)):
    for cel in row:
        if i == 0:
            cel.border = Border(top=sd1, bottom=sd1)
        else:
            cel.border = Border(bottom=sd2)
wb.save(fname)
