import openpyxl
wb = openpyxl.load_workbook('販売記録01.xlsx')
ws = wb.active
total = 0
for row in ws['A3:D8']:
    for cel in row:
        val = cel.value
        if isinstance(val, (int, float)):
            total += val
print(f'指定範囲の合計：{total}')
