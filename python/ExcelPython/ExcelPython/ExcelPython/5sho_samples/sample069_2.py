import openpyxl
fname = '注文記録10.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
tstl = ws.tables['注文'].tableStyleInfo
tstl.name = 'TableStyleLight6'
tstl.showFirstColumn=False
tstl.showLastColumn=True
tstl.showRowStripes=False
tstl.showColumnStripes=True
wb.save(fname)
