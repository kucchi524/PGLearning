import pandas as pd
import tkinter.filedialog as tk
from datetime import datetime
import os

fType = [("", "*")]
dir = "C:\\Users\\USER\\Desktop\\PG学習"
shift = tk.askopenfilename(title="シフト表を選んでください", initialdir=dir, filetypes=fType)
workin = tk.askopenfilename(title="勤務表を選んでください", initialdir=dir, filetypes=fType)

# 各ファイルを読み込む
sf = pd.read_excel(shift, sheet_name="シフト")
wf = pd.read_excel(workin, sheet_name="勤怠記録")

# 勤務開始と出勤時刻を読み込む
start = pd.to_datetime(sf["勤務開始"], format='%H:%M')
startWork = pd.to_datetime(wf["出勤時刻"], format='%H:%M')

# 社員IDをキーにしてマージする
merge = pd.merge(sf, wf, on="社員ID")

# 遅刻列を作成する
merge["遅刻"] = merge["出勤時刻"] > merge["勤務開始"]

# 遅刻者のみ抽出する
print(merge[merge["遅刻"] == True])