import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, 'メンバー情報08.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
ws = wb.ActiveSheet
ws.Range('D5:E6').Insert(Shift=-4121)
wb.Close(SaveChanges=True)
xlApp.Quit()
