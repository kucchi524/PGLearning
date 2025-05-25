import openpyxl
import re
fname = '営業所情報01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws.iter_rows(min_row=4):
    s = row[1].value
    result = re.match(r'(.+?)(\d.*)', s)
    if result:
        row[2].value = result.group(1)
        row[3].value = result.group(2)
wb.save(fname)
