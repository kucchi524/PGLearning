import openpyxl
import csv
bname = '販売記録07.xlsx'
tname = '記録テキスト01.csv'
wb = openpyxl.load_workbook(bname)
ws = wb.active
with open(tname, mode='w', newline='') as f:
    csvtext = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in ws.iter_rows(min_row=6, max_row=13):
        line = [cell.value for cell in row]
        csvtext.writerow(line)
