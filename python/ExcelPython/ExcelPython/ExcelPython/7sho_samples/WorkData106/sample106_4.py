import openpyxl
import csv
tname = '販売数追加.csv'
bname = '販売記録05.xlsx'
wb = openpyxl.load_workbook(bname)
ws = wb.active
with open(tname, mode='r') as f:
    csvdata = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for line in csvdata:
        ws.append(line)
wb.save(bname)
