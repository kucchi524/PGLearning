import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, '販売記録03.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
pc = wb.PivotCaches().Create(SourceType=1,
                             SourceData='販売データ')
pt = pc.CreatePivotTable(TableDestination=wb.Sheets('集計').Range('B2'),
                         TableName='販売集計')
pt.PivotFields('商品分類').Orientation = 1
pt.PivotFields('都道府県').Orientation = 2
pt.PivotFields('金額').Orientation = 4
pt.PivotFields('性別').Orientation = 3
pt.PivotFields('性別').CurrentPage = '女性'
wb.Close(SaveChanges=True)
xlApp.Quit()
