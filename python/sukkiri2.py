members = ['工藤', '松田', '浅木']
print(members)
print(members[0])

scores = [88, 90, 95]
total = sum(scores)
print(f'合計{total}点')
avg = total / len(scores)
print(f'平均{avg}点')

members.append('口石')
members.append('test')
print(members)

members.remove('test')
print(members)

a = [10, 20, 30, 40, 50]
print(a[1:3])
print(a[2:])
print(a[:3])

scores = {'network':60, 'database':80, 'security':50}
print(scores)
print(scores['database'])

scores['programming'] = 65
scores['security'] = 55
print(scores)

del scores['security']
print(scores)

total = sum(scores.values())
print(total)

scoresTuple = (70, 80, 55)
print(scoresTuple)
print(scoresTuple[0])
print(f'要素数は{len(scoresTuple)}')
print(f'合計は{sum(scoresTuple)}')

scoresSet = {70, 80, 55, 80}
scoresSet.add(80)
print(scoresSet)
print(f'要素数は{len(scoresSet)}')
print(f'合計は{sum(scoresSet)}')

scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
print(tuple(members))
print(list(scores))
print(set(scores.values()))

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print(c)
print(c[0])
print(c[1][2])

member_hobbies = {
    '松田': {'SNS', '麻雀', '自転車'},
    '浅木': {'麻雀', '食べ歩き', '数字', '数学', '数学'}
}
common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies)

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)