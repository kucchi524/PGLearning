ans = int(input('何点でしたか？'))
if ans >= 8:
    print('合格です')
elif ans >= 5:
    print('再挑戦が可能です')
else:
    print('不合格です')
