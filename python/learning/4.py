a = []
b = 0
for i in range(2):
    a.append(int(input('入力してください >>')))
    
print(len(a))

for j in range(len(a)):
    b = b + a[j]
    
print(b)