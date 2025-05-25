def tri_area(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

hen1 = float(input('辺Aの長さを入力'))
hen2 = float(input('辺Bの長さを入力'))
hen3 = float(input('辺Cの長さを入力'))
print(tri_area(hen1, hen2, hen3))
