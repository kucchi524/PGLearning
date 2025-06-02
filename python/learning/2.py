# BMI計算
height = int(input('身長(cm)を入力してください >>'))
weight = int(input('体重(kg)を入力してください >>'))
bmi = 0
height = float(height / 100)
bmi = float(weight / (height ** 2))
print(f'あなたのBMIは{bmi}です')

# 5教科平均点
natinalLanguage = int(input('国語の点数を入力してください >>'))
math = int(input('算数の点数を入力してください >>'))
science = int(input('理科の点数を入力してください >>'))
social = int(input('社会の点数を入力してください >>'))
english = int(input('英語の点数を入力してください >>'))
total = 0
results = [natinalLanguage, math, science, social, english]

for result in results:
    total = total + result

print(f'5教科の合計点は{total}点で、平均点は{float(total / len(results))}点です')