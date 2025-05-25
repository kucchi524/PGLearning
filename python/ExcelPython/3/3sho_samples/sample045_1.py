import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, 'メンバー情報04.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
ws = wb.ActiveSheet
ws.Range('A4:C10').Sort(Key1=ws.Range('C4'), Order1=2)
wb.Close(SaveChanges=True)
xlApp.Quit()
