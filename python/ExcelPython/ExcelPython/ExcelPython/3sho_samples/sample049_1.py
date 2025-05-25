import openpyxl
fname = 'メンバー情報06.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws['E3:E10']:
    for cel in row:
        cel.value = None
wb.save(fname)
