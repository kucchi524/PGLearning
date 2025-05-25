import openpyxl
from openpyxl.styles import Alignment
fname = '営業所情報03.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for cel in ws['B4:B8']:
    cel[0].alignment = Alignment(shrinkToFit=True, vertical='center')
wb.save(fname)
