import openpyxl
import datetime

wb = openpyxl.load_workbook('C:\\Users\\USER\\Desktop\\家計簿\\家計簿・改\\2025\\2025_家計簿.xlsm')
ws = wb['202506']
print(ws)

# 範囲を指定してnull以外の値を取得する
def cellNonNullValues (ws, startCell, endCell):
    cells = ws[startCell:endCell]
    return [
        cell.value
        for row in cells
        for cell in row
        if cell.value is not None
    ]
    
expences = cellNonNullValues(ws, 'A5', 'AG24')
income = cellNonNullValues(ws, 'A26', 'B31')

print('支出項目：', expences)
print('収入項目：', income)

tz = datetime.timezone(datetime.timedelta(hours=9))
dt = datetime.datetime.now(tz)

month = str()
day = str()
if dt.month < 10:
    month = str("0" + str(dt.month))

if dt.day < 10:
    day = str("0" + str(dt.day))

n = str(dt.year) + month + day
print(n)

expencesPath = 'C:\\Users\\USER\\Desktop\\家計簿\\家計簿・改\\テキストメモ\\' + n + '_支出.txt'
f = open(expencesPath, 'w')

for value in expences:
   f.write(str(value) + '\n')
f.close()

incomePath = 'C:\\Users\\USER\\Desktop\\家計簿\\家計簿・改\\テキストメモ\\' + n + '_収入.txt'
f = open(incomePath, 'w')
for value in income:
    f.write(str(value) + '\n')
f.close()