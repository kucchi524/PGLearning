import openpyxl
fname = '注文記録06.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws.iter_rows(min_row=4):
    row[0].number_format = 'yyyy年m月d日'
    row[1].number_format = 'h時m分'
wb.save(fname)
