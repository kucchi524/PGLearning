import openpyxl
fname = '見積明細書02.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws['A1'].style = 'Title'
wb.save(fname)
