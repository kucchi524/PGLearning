import os
import win32com.client
pname = os.path.dirname(__file__)
fname = os.path.join(pname, 'メンバー情報11.xlsx')
xlApp = win32com.client.Dispatch('Excel.Application')
wb = xlApp.Workbooks.Open(fname)
xlApp.Visible = True
rval = ['BD1243', '山本雄二', 27, '経営管理部','企画第3班']
wb.ActiveSheet.Range('A11:E11').Value = rval
wb.Close(SaveChanges=True)
xlApp.Quit()
