import openpyxl
import datetime
fname = '入荷予定04.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i in range(1, 6):
    ws.cell(i + 3, 3).value = datetime.date(2022, 1, i + 5)
wb.save(fname)
