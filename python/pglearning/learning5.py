import pandas as pd
import tkinter.filedialog as fd

iDir = "C:\\Users\\USER\\Desktop\\PG学習"
fTyp = [("", "*")]
readFile = fd.askopenfilename(title="CSVファイル選択", initialdir=iDir, filetypes=fTyp)

# ファイル読み込み
df = pd.read_csv(readFile)

# 空白除去
df = df.dropna(how="all")

# 氏名・部署のいずれかが空白なら除去
df = df.dropna(subset=["氏名", "部署"])

# 年齢が数値でない行を削除
df = df[df["年齢"].astype(str).str.isdigit()]
df["年齢"] = df["年齢"].astype(int)

# 入社日をdatetimeに変換
df["入社日"] = pd.to_datetime(df["入社日"], errors="coerce")

# 入社日が変換失敗になった行を削除
df = df[df["入社日"].notna()]

# 結果確認
print(df)

# エクセルファイルに保存
df.to_excel(iDir + "\\" + "従業員マスタ_未整形.xlsx", index=False)