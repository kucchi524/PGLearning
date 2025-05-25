import openpyxl
wb = openpyxl.load_workbook('店舗別10.xlsx')
print('シート数', len(wb.worksheets))
for i, ws in enumerate(wb.worksheets):
    cnum = 0
    for row in ws.iter_rows():
        for cell in row:
            if cell.value != None:
                cnum += 1
    print(i + 1, ws.title + '：入力セル数', cnum)
