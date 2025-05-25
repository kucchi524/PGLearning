import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, 'メンバー情報09.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
ws = wb.ActiveSheet
ws.Columns('B:C').Delete()
ws.Rows(7).Delete()
wb.Close(SaveChanges=True)
xlApp.Quit()
