import json
import pandas as pd

# fTpy = [("", "*")]
# iDir = "C:\\Users\\USER\\Desktop\\PG学習"
jsonFile = "C:\\PG練習\\python\\pglearning\\api.json"

with open(jsonFile, "r", encoding="utf-8") as f:
    data = json.load(f)
    devMembers = [emp for emp in data if emp["department"] == "開発部"]
    
    for emp in devMembers:
        print(f"{emp['name']} ({emp['age']} 歳) - {emp['department']} / 入社日: {emp['joined']}")
    
    df = pd.DataFrame(devMembers)
    df.to_excel("C:\\Users\\USER\\Desktop\\PG学習\\" + "開発部一覧.xlsx", index=False)
        