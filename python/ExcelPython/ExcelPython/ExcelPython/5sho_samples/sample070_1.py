import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, 'メンバー情報11.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
xlApp.Visible = True
wb = xlApp.Workbooks.Open(fname)
tbl = wb.ActiveSheet.ListObjects('メンバー')
nrow = tbl.ListRows.Add()
rval = ['BD1243', '山本雄二', 27, '経営管理部','企画第3班']
nrow.Range.Value = rval
wb.Close(SaveChanges=True)
xlApp.Quit()
