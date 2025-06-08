# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
count = int(input())
a = []
b = None
c = None
d = None
num = 0
for i in range(count):
    b = input()
    a.append(b)
    
for i in range(len(a)):
    results = a[i].split(' ')
    for j in range(len(results)):
        if j % 2 == 0:
            c = results[j]
        else:
            d = results[j]
            if (c == 'G' and d == 'C') or (c == 'C' and d == 'P') or (c == 'P' and d == 'G'):
                num += 1

print(num)