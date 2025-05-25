import requests
import pandas
res = requests.get('https://www.clayhouse.jp/cweb/books')
dfs = pandas.read_html(res.content)
with pandas.ExcelWriter('表記録.xlsx') as writer:
    for i, df in enumerate(dfs):
        df.to_excel(writer, index=False,
                    sheet_name= 'Sheet' + str(i + 1))
