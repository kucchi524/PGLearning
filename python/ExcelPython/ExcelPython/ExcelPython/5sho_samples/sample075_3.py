import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '売上記録03.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
chart = ws.Shapes.AddChart2(Style=-1, XlChartType=5,
                            Left=180, Top=30,
                            Width=250, Height=200).Chart
chart.SetSourceData(Source=ws.Range('A4:B7'))
chart.ChartTitle.Caption = '商品分類別売上'
wb.Close(SaveChanges=True)
xlApp.Quit()
