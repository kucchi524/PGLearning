import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '作図用02.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
ws.Shapes(2).Line.Weight = 6
ws.Shapes(2).Line.ForeColor.RGB = 192
wb.Close(SaveChanges=True)
xlApp.Quit()
