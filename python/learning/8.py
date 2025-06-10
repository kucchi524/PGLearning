count = 1
print('カレーを召し上がれ')

while count <= 100:
    print(f'{count}皿のカレーを食べました')
    answer = input('おかわりはいかがでしょうか >>')
    if answer == 'y':
        count += 1
    else:
        print('ごちそうさまでした')
        break
    
for i in range(1, 12):
    if i >= 11:
        print('Lift off!!')
    else:
        print(f'{i}、', end='')
        
for j in range(11):
    if j < 10:
        print(f'{10 - j}、', end='')
    else:
        print('Lift off!!')