import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '営業所情報02.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
ws = wb.ActiveSheet
ws.Range('A3:A8').Copy(Destination=ws.Range('D3:D8'))
wb.Close(SaveChanges=True)
xlApp.Quit()
