import openpyxl
fname = 'メンバー情報02.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
for row in ws.iter_rows():
    for cel in row:
        s = str(cel.value)
        if '開発' in s:
            cel.value = s.replace('開発', '企画')
wb.save(fname)
