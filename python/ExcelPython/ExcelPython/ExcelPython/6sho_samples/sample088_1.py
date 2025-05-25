import openpyxl
fname = '店舗別07.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.copy_worksheet(wb['販売数2月'])
ws.title = '予備データ'
wb.save(fname)
