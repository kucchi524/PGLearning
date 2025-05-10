name = input('あなたの名前を教えてください >> ')
print(f'{name}さんこんにちは')
food = input('好きな食べ物を教えてください >> ')
if food == 'カレー':
    print('素敵です。カレーは最高ですよね！！')
else:
    print(f'私も{food}が好きですよ')
    
name = input('あなたの名前を教えてください >> ')
print(f'{name}さんこんにちは')
food = input('好きな食べ物を教えてください >> ')
if 'カレー' in food:
    print('素敵です。カレーは最高ですよね！！')
else:
    print(f'私も{food}が好きですよ')
    
scores = [80, 100, 20, 60]
if 100 in scores:
    print('100点満点の試験があったんですね。おめでとう！')
else:
    print('次はどれか1つでも100点満点を取ろう')
    
scores = {'network': 60, 'database': 80, 'security': 50}
key = input('追加する科目を入力してください >> ')
if key in scores:
    print('既に登録済です')
else:
    data = input('得点を入力してください >> ')
    scores[key] = data
print(scores)

score = int(input('点数を入力してください >> '))
if score < 0 or score > 100:
    print('異常な点数です')
    print('入力しなおしてください')
elif score >= 60:
    print('合格！')
    print('よく頑張りました')
else:
    print('残念ながら不合格です')
    print('追試を受けてください')
