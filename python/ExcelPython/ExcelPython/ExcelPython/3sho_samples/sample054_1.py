import openpyxl
wb = openpyxl.load_workbook('成績表02.xlsx')
ws = wb.active
vdic = {}
for row in ws.iter_rows(min_row=4):
    vdic[row[0].value] = sum([cel.value for cel in
                              row[1:]])
    mv = max(vdic.values())
    top = [k for k, v in vdic.items() if v == mv]
print(f'最高点：{mv}')
print(f'第1位：{top[0]}')
