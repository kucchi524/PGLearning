import openpyxl
from openpyxl.styles import Alignment
fname = '注文記録08.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i, row in enumerate(ws.iter_rows(min_row=3)):
    if i == 0:
        for cel in row:
            cel.alignment = Alignment(horizontal='center',
                                      vertical='bottom')
    else:
        row[0].alignment = Alignment(horizontal='left',
                                     vertical='center')
wb.save(fname)
