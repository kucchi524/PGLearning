import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '作図用01.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
ws.Shapes.AddShape(9, 30, 50, 150, 100)
wb.Close(SaveChanges=True)
xlApp.Quit()
