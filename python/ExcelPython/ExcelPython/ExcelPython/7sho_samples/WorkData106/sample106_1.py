import openpyxl
tname = '追加店舗.csv'
bname = '店舗リスト01.xlsx'
wb = openpyxl.load_workbook(bname)
ws = wb.active
with open(tname, mode='r') as f:
    lines = f.read().splitlines()
    for line in lines:
        nline = line.split(',')
        ws.append(nline)
wb.save(bname)
