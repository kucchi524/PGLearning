import openpyxl
fname = '入荷予定08.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
ws.print_area = 'A1:F9'
ws.oddFooter.center.text = '&D'
ws.oddFooter.size = 14
ws.oddFooter.font = 'メイリオ'
ws.page_setup.orientation = 'landscape'
ws.page_setup.paperSize = 13
wb.save(fname)
