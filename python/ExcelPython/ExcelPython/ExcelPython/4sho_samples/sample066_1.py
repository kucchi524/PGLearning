import openpyxl
from openpyxl.styles import Font
from openpyxl.formatting.rule import CellIsRule
fname = '成績表03.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
fnt = Font(color='00008B', bold=True)
nrule = CellIsRule(operator='greaterThanOrEqual', formula=[90],
                   stopIfTrue=None, font=fnt)
ws.conditional_formatting.add('B4:D8', nrule)
wb.save(fname)
