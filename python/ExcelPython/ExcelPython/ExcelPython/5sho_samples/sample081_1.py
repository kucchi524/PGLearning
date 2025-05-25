import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '販売記録04.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
ws = wb.ActiveSheet
pc = wb.PivotCaches().Create(SourceType=1, SourceData='販売データ')
pt = pc.CreatePivotTable(TableDestination=
                         wb.Sheets('集計').Range('B2'),
                         TableName='販売集計')
chart = ws.Shapes.AddChart2(Style=-1, XlChartType=51,
                            Left=320, Top=30,
                            Width=350, Height=280).Chart
chart.SetSourceData(Source=pt.TableRange1)
chart.HasTitle = True
chart.ChartTitle.Caption = '販売データ集計'
pt.PivotFields('都道府県').Orientation = 1
pt.PivotFields('商品分類').Orientation = 2
pt.PivotFields('金額').Orientation = 4
wb.Close(SaveChanges=True)
xlApp.Quit()
