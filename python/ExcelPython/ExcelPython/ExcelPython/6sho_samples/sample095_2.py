import openpyxl
from openpyxl.workbook.protection import WorkbookProtection
fname = '店舗別11.xlsx'
pword = 'excel2021'
wb = openpyxl.load_workbook(fname)
wb.security = WorkbookProtection()
wb.security.workbook_password = pword
wb.security.lockStructure = False
wb.save(fname)
