import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '商品別推移01.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
for tbl in ws.ListObjects:
    crng = tbl.Range
    chart = ws.Shapes.AddChart2(Style=-1, XlChartType=4,
                                Left=crng.Left,
                                Top=crng.Range('A5').Top,
                                Width=crng.Width,
                                Height=112.5).Chart
    chart.SetSourceData(Source=tbl.Range)
    chart.PlotBy = 1
    chart.HasTitle = False
    chart.HasLegend = False
wb.Close(SaveChanges=True)
xlApp.Quit()
