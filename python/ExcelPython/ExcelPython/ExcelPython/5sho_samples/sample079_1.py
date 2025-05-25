import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '売上記録06.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
for cobj in wb.ActiveSheet.ChartObjects():
    cobj.Width = cobj.Width + 10
    cobj.Height = cobj.Height + 10
    chart = cobj.Chart
    dlabel = chart.FullSeriesCollection(1).DataLabels()
    fnt = dlabel.Format.TextFrame2.TextRange.Font
    fnt.Fill.ForeColor.RGB = 16777215
    chart.HasLegend = False
wb.Close(SaveChanges=True)
xlApp.Quit()
