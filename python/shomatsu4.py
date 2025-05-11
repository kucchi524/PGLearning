count = 1
print('カレーを召し上がれ')
while count <= 100:
    print(f'{count}皿のカレーを食べました')
    flg = input('おかわりはいかがですか？ (y/n) >> ')
    if flg == 'y':
        count += 1
    else:
        break
print('ごちそうさまでした')

for count in range(11):
    if count == 0:
        continue
    print(f'{count}、',end='')
    if count == 10:
        print('Lift off!')
        
for count in range(10):
    if count % 2 == 0:
        continue
    else:
        for num in range(10):
            if count * num == 0:
                continue
            if count * num > 50:
                continue
            print(count * num)

temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]
for data in temp:
    print(data)
    
temp_new = [7.8, 9.1, 10.2, 11.0, 12.5, 'N/A', 14.3, 13.8, 12.9, 12.4]
tempList = list()
for data in temp_new:
    print(data)
    if isinstance(data, float):
        tempList.append(data)
total = sum(tempList)
print(f'平均気温は{total / len(tempList)}℃です')
