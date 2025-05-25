import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '販売記録02.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
wb.Names.Add('全店合計', '=Sheet1!$E$4:$E$8')
wb.Close(SaveChanges=True)
xlApp.Quit()
