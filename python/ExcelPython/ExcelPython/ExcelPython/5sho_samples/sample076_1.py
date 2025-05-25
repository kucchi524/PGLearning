import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '店舗別01.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
cobj = ws.ChartObjects(1)
rng = ws.Range('F3:K14')
cobj.Left = rng.Left
cobj.Top = rng.Top
cobj.Width = rng.Width
cobj.Height = rng.Height
wb.Close(SaveChanges=True)
xlApp.Quit()
