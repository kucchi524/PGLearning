import openpyxl
from openpyxl.styles import NamedStyle, Font
from openpyxl.styles.borders import Border, Side
fname = '見積明細書03.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
fnt = Font(name='Book Antiqua', color='000080', italic=True)
bdr = Border(bottom=Side(style='thin', color='00BFFF'))
nstl = NamedStyle(name='データ', font=fnt, border=bdr)
for row in ws['A4:E6']:
    for cel in row:
        cel.style = nstl
wb.save(fname)
