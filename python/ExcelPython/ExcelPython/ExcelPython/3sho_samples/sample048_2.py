import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '成績表01.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
ws = wb.ActiveSheet
ws.Range('A2:E7').Cut(Destination=ws.Range('C4'))
wb.Close(SaveChanges=True)
xlApp.Quit()
