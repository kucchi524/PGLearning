def bmi(weight, height):
    return weight / height ** 2

w = float(input('体重を入力してください（kg単位）'))
h = float(input('身長を入力してください（m単位）'))
if bmi(w, h) >= 25:
    print('肥満です')
else:
    print('肥満ではありません')
