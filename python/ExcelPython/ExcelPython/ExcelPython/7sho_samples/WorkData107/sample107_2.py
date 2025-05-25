import pandas
bname = '販売記録07.xlsx'
tname = '記録テキスト02.csv'
df = pandas.read_excel(bname, header=5, skipfooter=1)
df.to_csv(tname, index=False, encoding='shift-jis')
