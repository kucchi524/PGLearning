import os
import win32com.client
pname = os.path.dirname(__file__)
fname1 = os.path.join(pname, '店舗別07.xlsx')
fname2 = os.path.join(pname, '販売数前月分.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb1 = xlApp.Workbooks.Open(fname1)
wb2 = xlApp.Workbooks.Open(fname2)
xlApp.Visible = True
wb1.Sheets('販売数1月').Copy(Before=wb2.Sheets(1))
wb2.Close(SaveChanges=True)
xlApp.Quit()
