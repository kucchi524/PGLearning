def hello():
    print('こんにちは')
    
hello()

def hello2(name):
    print(f'こんにちは。{name}です。')
    
hello2('カビゴン')
hello2('口石')

def profile(name, age, hobby):
    print(f'私の名前は{name}です。')
    print(f'年齢は{age}歳です。')
    print(f'趣味は{hobby}です。')
    
profile('カビゴン', 28, '大食い')

def plus(x, y):
    answer = x + y
    return answer

answer = plus(100, 50)
print(f'足し算の答えは{answer}です。')

def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点？ >>'))
    database = int(input('ネットワークの得点？ >>'))
    security = int(input('ネットワークの得点？ >>'))
    scores = [network, database, security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print(f'{name}さんの平均点は{avg}点です。')
    
asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)

def eat(breakfast, lunch, dinner='カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')
    
print('8/1')
eat('トースト', 'おにぎり')
print('8/2')
eat('納豆ご飯', 'ラーメン')
print('8/3')
eat('ばなな', 'そば', '焼肉')
print('8/4')
eat('サンドウィッチ', 'シュウマイ弁当')

def eat2(breakfast, lunch, dinner='カレー', *desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'夜は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')

eat2('家系ラーメン', '二郎系ラーメン', '長浜ラーメン', 'パフェ', 'ケーキ', 'アイス')

name = '松田'
def change_name():
    global name
    name = '浅木'
    
def hello():
    print('こんにちは' + name + 'さん')
    
change_name()
hello()

