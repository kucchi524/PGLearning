import openpyxl
fname = '入荷予定07.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.protection.password = 'excel'
ws.protection.disable()
wb.save(fname)
