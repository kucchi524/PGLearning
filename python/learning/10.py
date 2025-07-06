a = []
for i in range(2):
    a.append(input())
    
count = int(a[0])
boxes = a[1].split(" ")
boxes = list(map(int, boxes))

avg = sum(boxes) / count

if avg == int(avg):
    print(int(avg))
else:
    avg = avg + 1
    print(int(avg))