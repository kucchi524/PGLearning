import openpyxl
import json
fname = 'メニュー一覧01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
with open('itemlist01.json', 'r') as f:
    jdata = json.load(f)
for category in jdata['category']:
    for item in category['items']:
        line = [category['name'],
                item['name'],
                item['price']]
        ws.append(line)
wb.save(fname)
