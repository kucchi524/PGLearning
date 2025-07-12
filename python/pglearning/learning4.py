import tkinter.filedialog as tk
import pandas as pd
import os

fType = [("", "*")]
iDir = "C:\\Users\\USER\\Desktop\\PG学習"
files = tk.askopenfilenames(title="CSVファイルを選んでください", filetypes=fType, initialdir=iDir)

dfs =[]

for file in files:
    if file.endswith(".csv"):
        df = pd.read_csv(file)
        dfs.append(df)
        
merged_df = pd.concat(dfs, ignore_index=True)

print(merged_df.head)
merged_df.to_excel(iDir + "\\" + "結合結果.xlsx", index=False)