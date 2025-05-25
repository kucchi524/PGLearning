import openpyxl
wb = openpyxl.load_workbook('販売記録01.xlsx')
ws = wb.active
for row in ws.iter_rows():
    for cel in row:
        if isinstance(cel.value, (int, float)):
            print(cel.coordinate, cel.value, sep='：')
