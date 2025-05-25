import pandas as pd
fname = '成績表02.xlsx'
edata = pd.read_excel(fname, index_col=0, sheet_name=0,
                      skiprows=2)
emean = edata.mean()
print(emean['数学'])
