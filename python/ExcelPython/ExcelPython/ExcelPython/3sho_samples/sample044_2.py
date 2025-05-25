import openpyxl
wb = openpyxl.load_workbook('販売記録02.xlsx')
aname = '作業範囲'
ndst = wb.defined_names[aname].destinations
total = 0
for tab, crd in ndst:
    ws = wb[tab]
    for rw in ws[crd]:
        for cel in rw:
            val = cel.value
            if isinstance(val, (int, float)):
                total += val
print(f'指定範囲の合計：{total}')
