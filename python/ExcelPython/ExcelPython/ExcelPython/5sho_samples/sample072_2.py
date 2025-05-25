import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '作図用01.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
rng = ws.Range('F3:H6')
ws.Shapes.AddShape(5, rng.Left, rng.Top, rng.Width, rng.Height)
wb.Close(SaveChanges=True)
xlApp.Quit()
