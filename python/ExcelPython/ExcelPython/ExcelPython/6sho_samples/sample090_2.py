import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '店舗別08.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
xlApp.Visible = True
wb = xlApp.Workbooks.Open(fname)
wb.Sheets('販売数2月').PrintPreview()
