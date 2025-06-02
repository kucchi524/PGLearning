a = {'筋トレ', 'ギター', 'ドライブ', '歴史巡り', '料理'}
b = {'乗り鉄', '撮り鉄', '音鉄', 'ギター', 'ドライブ'}
print(input('心の準備ができたらenterキーを押してください'))
print(f'相性度: {len(a & b) / len((a | b)) * 100}%')

n = 99
isError = False

if isError == False & n < 100:
    print('terst')
    
num = int(input('数値を入力してください >>'))
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')
    
greeting = input('挨拶を入力してください >>')

if greeting == 'こんにちは':
    print('ようこそ！')
elif greeting == '景気は？':
    print('ぼちぼちです')
elif greeting == 'さようなら':
    print('お元気で！')
else:
    print('どうしました？')