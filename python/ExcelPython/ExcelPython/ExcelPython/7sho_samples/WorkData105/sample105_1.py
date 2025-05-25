import openpyxl
import glob
bname = '選抜メンバー03.xlsx'
tname = '選手リスト.txt'
wb = openpyxl.load_workbook(bname)
ws = wb.active
text = []
for row in ws.iter_rows(min_row=4):
    text.append(row[1].value)
with open(tname, mode='w') as f:
    f.write('\n'.join(text))
