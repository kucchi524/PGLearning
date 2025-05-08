height = float(input('身長を入力してください >> '))
weight = float(input('体重を入力してください >> '))
height = height / 100
bmi = weight / height / height
print('あなたのBMIは' + str(bmi) + 'です')