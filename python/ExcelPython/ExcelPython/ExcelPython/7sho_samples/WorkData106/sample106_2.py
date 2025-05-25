import openpyxl
tname = '成績追加分.csv'
bname = '成績記録04.xlsx'
wb = openpyxl.load_workbook(bname)
ws = wb.active
with open(tname, mode='r') as f:
    lines = f.read().splitlines()
    for line in lines:
        nline = line.split(',')
        ws.append(nline)
wb.save(bname)
