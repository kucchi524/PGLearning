import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, 'メンバー情報05.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
ws = wb.ActiveSheet
ws.Range('A3').AutoFilter(Field=3, Criteria1='>=35')
wb.Close(SaveChanges=True)
xlApp.Quit()
