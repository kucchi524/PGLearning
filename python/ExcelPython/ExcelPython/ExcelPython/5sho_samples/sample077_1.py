import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '店舗別02.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
chart = wb.ActiveSheet.ChartObjects(1).Chart
tfnt = chart.ChartTitle.Format.TextFrame2.TextRange.Font
tfnt.Size = 18
tfnt.NameFarEast = 'メイリオ'
chart.ChartArea.Format.Fill.ForeColor.RGB = 14218471
chart.Legend.Position =  -4152
wb.Close(SaveChanges=True)
xlApp.Quit()
