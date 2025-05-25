import openpyxl
from openpyxl.workbook.protection import WorkbookProtection
fname = '店舗別11.xlsx'
pword = 'excel2021'
wb = openpyxl.load_workbook(fname)
wb.security = WorkbookProtection()
wb.security.lockStructure = True
wb.security.workbook_password = pword
wb.save(fname)
