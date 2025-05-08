print(1)
print(10)

print(1 + 1)
print(10 - 2)
print('1' + '1')
print('python' + 'の世界へようこそ')
print('pythonは' + 'とっても' * 3 +'楽しいですよ')
print('はじめまして松田です。身体を動かすのが好きです')
print('はじめまして\n松田です\n身体を動かすのが好きです')
print('引用符には、\'と"があります')
print('''はじめまして
      松田です
      身体を動かすのが好きです''')
print('''はじめまして
      松田です
      身体を動かすのが好きです'''.strip())
name = '松田'
age = 22
print(name)
print(age)
print('半径3cmの直径は')
dia = 3 * 2
print(dia)
print('その円の長さは')
circle = dia *3.14
print(circle)
name, age = '口石', 33
print('現在の' + name + 'は')
print(age)
print('もうすぐ')
age = age + 1
print(age)
print('来年は')
age = age + 1
print(age)
name=input('あなたの名前を入力してください')
print('おお、' + name +'よ。そなたが来るのを待っておったぞ')
x = 3.14
y = int(x)
print(y)
z = str(x)
print(z)
print(type(z))
print(z * 2)
price=input('値段を入力してください >>')
price=int(price)
number = input('人数を入力してください >>')
number = int(number)
payment = price * number
print('お支払金額は' + str(payment) + '円です')
name = '口石凌'
age = 33
height = 167.0
print('私は{}、身長は{}で、年齢は{}です'.format(name, height, age))
print(f'私は{name}、年齢は{age}で、身長は{height}です')

weight=input('体重を入力してください >>')
height=input('身長を入力してください >>')
height=float(height) / 100
bmi = float(weight) / height / height
print('あなたのBMIは' + str(bmi) + 'です')