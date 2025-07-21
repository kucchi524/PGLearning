import pandas as pd
import datetime as dt
import tkinter.filedialog as fd

iDir = "C:\\Users\\USER\\Desktop\\PG学習"
fTyp = [("", "*")]
readFile = fd.askopenfilename(title="読み込むファイルを選んでください", initialdir=iDir, filetypes=fTyp)

df = pd.read_excel(readFile)

summary = df.groupby("部署").agg(
    人数=("氏名", "count"),
    平均年齢=("年齢", "mean")
).reset_index()

today = dt.datetime.today().strftime("%y%m%d")
reportFile = f"{iDir}\\{today}_レポート.xlsx"

with pd.ExcelWriter(reportFile, engine="xlsxwriter") as writer:
    summary.to_excel(writer, sheet_name="部署別集計", index=False)
    df.to_excel(writer, sheet_name="原本データ", index=False)
    
print(f"{readFile}を作成しました")