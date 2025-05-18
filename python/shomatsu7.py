file = open('test1.txt', 'r')
copy = open('copy.txt', 'w')
for line in file:
    copy.write(line)
file.close()
file.close()