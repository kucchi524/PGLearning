count = 0
while count < 3:
    count += 1
    print(f'ひつじが{count}匹')
print('おやすみなさい')

is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f'ひつじが{count}匹')
    key = input('もう眠りそうですか？(y/n) >> ')
    if key == 'y':
        is_awake = False
print('おやすみなさい')

count = 0
student_num = int(input('学生の数を入力 >> '))
score_list = list()
while count < student_num:
    count += 1
    score = int(input(f'{count}人目の試験の得点を入力 >> '))
    score_list.append(score)
print(score_list)
total = sum(score_list)
print(f'平均点は{total / student_num}点です')

scores = [80, 20, 75, 60]
count = 0
while count < len(scores):
    if scores[count] >= 60:
        print('合格')
    else:
        print('不合格')
    count += 1
for data in scores:
    if data >= 60:
        print('合格')
    else:
        print('不合格')
    
for num in range(3):
    print('pythonは楽しい')
    
ages = [28, 50, 8, 20, 78, 25, 22, 10, 27, 33]
num = 5
samples = list()
for data in ages:
    if 20 <= data < 30:
        samples.append(data)
        if len(samples) == num:
            break
print(samples)

ages = [28, 50, 'ひみつ', 20, 78, 25, 22, 10, '無回答', 33]
samples = list()
for data in ages:
    if not isinstance(data, int):
        continue
    if data < 20 or data >= 30:
        continue
    samples.append(data)
print(samples)