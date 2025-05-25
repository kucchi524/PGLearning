import openpyxl
fname = '入荷予定01.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for i, cel in enumerate(ws['A4:A8']):
    cel[0].value = i + 1
wb.save(fname)
