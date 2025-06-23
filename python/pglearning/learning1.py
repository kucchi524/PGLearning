import pandas as pd
import tkinter.filedialog
import os

fType = [("", "*")]
dir = os.path.abspath(__file__)
filename = tkinter.filedialog.askopenfilename(filetypes=fType, initialdir=dir)
saveFilename = tkinter.filedialog.asksaveasfilename(title="ファイル保存", initialdir=dir, defaultextension="xlsx")

# excelからデータを読み込む
df = pd.read_excel(filename, sheet_name="従業員マスタ")

# 「営業部」のデータを抽出
eigyo_df = df[df["部署"] == "営業部"]

# 営業部のデータを新しいエクセルに保存
eigyo_df.to_excel(saveFilename, index=False)