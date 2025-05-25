import openpyxl
import datetime
fname = '注文記録03.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
dt = datetime.date(2022, 1, 6)
tm = datetime.time(16, 25, 0)
ad_data = [dt, tm, '海鮮セットB', 3200, 1]
ws.append(ad_data)
wb.save(fname)
