import openpyxl
from openpyxl.worksheet.datavalidation import DataValidation
fname = '注文記録09.xlsx'
wb = openpyxl.load_workbook(fname)
ws = wb.active
dv = DataValidation(type='whole', operator='between',
                    formula1=1, formula2=5)
dv.errorTitle = '注文数の問題'
dv.error = '注文できるのは5個までです。'
dv.promptTitle = '注文数入力'
dv.prompt = '注文数を入力してください。'
dv.add('E4:E9')
ws.add_data_validation(dv)
wb.save(fname)
