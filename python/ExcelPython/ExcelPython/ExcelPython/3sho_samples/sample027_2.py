import openpyxl
import sys
wb = openpyxl.load_workbook('販売記録01.xlsx')
ws = wb.active
for row in ws.iter_rows(min_row=4):
    for cel in row:
        val = cel.value
        if isinstance(val, (int, float)):
            print(cel.coordinate, val, sep='：')
            sys.exit()
