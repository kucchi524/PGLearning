import openpyxl
import json
fname = 'メニュー一覧02.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
with open('itemlist02.json', 'r') as f:
    jdata = json.load(f)
for row in ws.iter_rows(min_row=4):
    tcat = [x for x in jdata['category']
            if x['name'] == row[0].value][0]
    aitem = {'name':row[1].value,
             'price':row[2].value}
    tcat['items'].append(aitem)
with open('itemlist03.json', 'w') as fw:
    json.dump(jdata, fw, ensure_ascii=False)
