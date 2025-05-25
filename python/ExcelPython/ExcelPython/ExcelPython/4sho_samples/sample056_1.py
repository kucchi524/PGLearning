import openpyxl
fname = '注文記録04.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws['A1'].font = openpyxl.styles.fonts.Font(name='メイリオ', size=14)
wb.save(fname)
