import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '売上記録05.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
srcs = ['A1', 'A8', 'F1', 'F8']
for src in srcs:
    srng = ws.Range(src)
    chart = ws.Shapes.AddChart2(Style=-1, XlChartType=5,
                                Left=srng.Left + 120,
                                Top=srng.Top + 10,
                                Width=130,
                                Height=110).Chart
    chart.SetSourceData(Source=srng.Range('A3:B6'))
    chart.HasTitle = False
wb.Close(SaveChanges=True)
xlApp.Quit()
