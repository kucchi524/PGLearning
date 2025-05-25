import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '作図用03.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
ws.Shapes('楕円 1').TextFrame2.TextRange.Text = 'Excel 2019'
wb.Close(SaveChanges=True)
xlApp.Quit()
