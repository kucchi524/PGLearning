import openpyxl
import sys
wb = openpyxl.load_workbook('販売記録01.xlsx')
ws = wb.active
for row in ws.iter_rows(min_row=4, max_col=5):
    for cel in row:
        if isinstance(cel.value, str):
            if '支店' in cel.value:
                print(cel.coordinate, cel.value, sep='：')
                sys.exit()
