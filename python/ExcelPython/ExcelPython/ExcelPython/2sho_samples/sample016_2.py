try:
    ans = int(input('本体価格を入力してください。'))
    price = int(ans * 1.1)
    print(f'税込価格　{price}円')
except:
    print('入力値が不適切です。')
