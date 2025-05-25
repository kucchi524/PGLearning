import openpyxl
from openpyxl.formatting.rule import DataBarRule
fname = '成績表03.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
nrule = DataBarRule(start_type='num', start_value=0,
                    end_type='num', end_value=300,
                    color='00FFFF',
                    minLength=0, maxLength=100)
ws.conditional_formatting.add('E4:E8', nrule)
wb.save(fname)
