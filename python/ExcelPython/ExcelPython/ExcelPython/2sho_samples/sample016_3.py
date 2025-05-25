try:
    ans = int(input('人数を入力してください。'))
    share = int(100000 / ans)
    print(f'1人当たり　{share}円')
except ValueError:
    print('入力値が不適切です。')
except ZeroDivisionError:
    print('0は指定できません。')

