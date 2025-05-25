import openpyxl
wb = openpyxl.load_workbook('販売記録02.xlsx')
aname = '横浜支店'
narea = wb.defined_names[aname].attr_text
print(f'{aname}の範囲：{narea}')
