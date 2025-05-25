import openpyxl
import re
wb = openpyxl.load_workbook('販売記録01.xlsx')
ws = wb.active
for row in ws.iter_rows():
    for cel in row:
        result = re.match('(.{3})本店', str(cel.value))
        if result:
            print(cel.coordinate, result.group(1), sep='：')
