import openpyxl
fname = '店舗別04.xlsx'
wb = openpyxl.load_workbook(fname)
wb['販売数2月'].sheet_state = 'visible'
wb.worksheets[-1].sheet_state = 'visible'
wb.save(fname)
