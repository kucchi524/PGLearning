import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '販売記録03.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
pt = wb.Sheets('集計').PivotTables('販売集計')
pt.ClearTable()
pt.PivotFields('都道府県').Orientation = 1
pt.PivotFields('性別').Orientation = 2
pt.PivotFields('年齢').Orientation = 4
pt.DataFields(1).Function = -4106
wb.Close(SaveChanges=True)
xlApp.Quit()
