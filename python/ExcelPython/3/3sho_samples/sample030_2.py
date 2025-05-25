import openpyxl
wb = openpyxl.load_workbook('販売記録01.xlsx',
                            data_only=True)
ws = wb.active
for row in ws.iter_rows(min_row=4, max_row=8, max_col=5):
    sval = row[0].value
    if sval.endswith('本店'):
        vals = []
        for cel in row:
            vals.append(str(cel.value))
        print('/'.join(vals))
