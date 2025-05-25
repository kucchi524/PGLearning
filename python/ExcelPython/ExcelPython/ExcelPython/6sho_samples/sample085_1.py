import openpyxl
fname = '店舗別05.xlsx'
wb = openpyxl.load_workbook(fname)
wb.remove(wb['4月分'])
wb.save(fname)
