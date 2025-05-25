import pandas
fname = '売上データ.csv'
bname = '販売記録06.xlsx'
df = pandas.read_csv(fname, encoding='shift-jis')
df.to_excel(bname, index=False)
