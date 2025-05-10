isError = True
n = 90

if isError == False and n < 100:
    print('画面表示')
    
num = int(input('数値を入力してください >> '))
if num % 2 == 0:
    print(f'{num}は偶数')
else:
    print(f'{num}は奇数')
    
greeting = input('あいさつを入力してください >> ')
if greeting == 'こんにちは':
    print('ようこそ')
elif greeting == '景気は？':
    print('ぼちぼちです')
elif greeting == 'さようなら':
    print('お元気で！')
else:
    print('どうしました？')