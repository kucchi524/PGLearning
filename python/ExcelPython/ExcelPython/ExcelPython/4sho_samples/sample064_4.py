import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '見積明細書02.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
ws.Range('A1').Style = 'タイトル'
ws.Range('A3:E3').Style = '見出し 3'
ws.Range('C7:E7').Style = '集計'
wb.Close(SaveChanges=True)
xlApp.Quit()
