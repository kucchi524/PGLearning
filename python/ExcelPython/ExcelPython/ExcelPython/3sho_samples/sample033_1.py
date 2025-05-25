import openpyxl
import datetime
fname = '注文記録02.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws['A8'].value = datetime.date(2022, 1, 6)
wb.save(fname)
