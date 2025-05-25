import openpyxl
fname = '店舗別03.xlsx'
wb = openpyxl.load_workbook(fname)
wb['Sheet2'].title = '販売数2月'
ws = wb.worksheets[2]
ws.title = '販売数' + ws.title[:2]
wb.save(fname)
