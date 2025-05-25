import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo
fname = 'メンバー情報10.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
tbl = Table(displayName='情報', ref='A3:E10')
sinfo = TableStyleInfo(name='TableStyleMedium7',
                       showFirstColumn=True,
                       showLastColumn=False,
                       showRowStripes=True,
                       showColumnStripes=False)
tbl.tableStyleInfo = sinfo
ws.add_table(tbl)
wb.save(fname)
