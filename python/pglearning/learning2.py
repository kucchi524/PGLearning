import pandas as pd
import tkinter.filedialog as tk
import os

fType = [("", "*")]
dir = os.path.abspath("C:\\Users\\USER\\Desktop\\PG学習")
readfile = tk.askopenfilename(filetypes=fType, initialdir=dir)

# excelファイルを読み込む
df = pd.read_excel(readfile, sheet_name="従業員マスタ")

# 部署ごとの人数を出す
print(df.groupby("部署").size())

# 平均年齢を出す
print(round(df.groupby("部署")["年齢"].mean()))

# 部署・性別ごとの人数をクロス集計
print(df.groupby(["部署", "性別"]).size())

# 平均30歳未満の部署を出す
avg = round(df.groupby("部署")["年齢"].mean())
print(avg[avg < 30])

# ピボットテーブル形式で部署ごとの性別別人数を出力
print(pd.pivot_table(df, index="部署", columns="性別", values="社員ID",  aggfunc="count", fill_value=0))