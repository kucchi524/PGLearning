import openpyxl
import datetime
fname = '注文記録02.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws['B8'].value = datetime.time(14, 42, 0)
wb.save(fname)
