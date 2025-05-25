import openpyxl
wb = openpyxl.load_workbook('成績表02.xlsx')
ws = wb.active
vdic = {}
for col in ws.iter_cols(min_col=2, min_row=3):
    vdic[col[0].value] = sum([cel.value for cel in col[1:]]) / len(col[1:])
print(vdic)
