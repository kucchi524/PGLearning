def is_number(moji):
    try:
        float(moji)
    except ValueError:
        return False
    else:
        return True

w = input('体重を入力してください（kg単位）')
h = input('身長を入力してください（m単位）')
if is_number(w) and is_number(h):
    if bmi(float(w), float(h)) >= 25:
        print('肥満です')
    else:
        print('肥満ではありません')
else:
    print('BMIが計算できません')
