num = int(input('数値を入力してください >>'))

def is_leapyear(year):
    if year % 400 == 0:
        print(f'西暦{year}年は、うるう年です。')
    elif year % 4 == 0 and year % 100 != 0:
        print(f'西暦{year}年は、うるう年です。')
    else:
        print(f'西暦{year}年は、うるう年ではありません。')

is_leapyear(num)