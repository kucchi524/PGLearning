import openpyxl
fname = '店舗別03.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.title = '販売数1月'
wb.save(fname)
