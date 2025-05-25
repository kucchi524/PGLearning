import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '店舗別09.xlsx')
pfname = fname[:-4] + 'pdf'
xlApp = win32com.client.Dispatch('Excel.Application')
xlApp.Visible = True
wb = xlApp.Workbooks.Open(fname)
wb.ActiveSheet.ExportAsFixedFormat(Type=0,
                                   Filename=pfname)
xlApp.Quit()
