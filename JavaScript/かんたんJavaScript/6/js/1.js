var names = ['高橋', '佐藤', '佐々木', '鈴木', '小松']
console.log(names[3])

names[3] = '小野寺'
console.log(names[3])

names = ['高橋', '佐藤', '佐々木', '鈴木', '小松']
for (let i = 0; i < names.length; i++) {
  console.log(names[i])
}

for (let val of names) {
  console.log(val)
}

var array2D = [
  ['A', 'B', 'C', 'D'],
  ['E', 'F', 'G', 'H'],
]
console.log(array2D[0][0])
console.log(array2D[0][1])
console.log(array2D[0][2])
console.log(array2D[0][3])
console.log(array2D[1][0])
console.log(array2D[1][1])
console.log(array2D[1][2])
console.log(array2D[1][3])

for (let array1D of array2D) {
  for (let val of array1D) {
    console.log(val)
  }
}

var jagged3D = [
  [
    ['A', 'B', 'C'],
    ['D', 'E', 'F', 'G'],
  ],
  [
    ['H', 'I', 'J', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
  ],
]
console.log(jagged3D[0][0][2])
console.log(jagged3D[0][1][3])
console.log(jagged3D[1][0][3])
console.log(jagged3D[1][1][4])
for (let jagged2D of jagged3D) {
  for (let jagged1D of jagged2D) {
    for (let val of jagged1D) {
      console.log(val)
    }
  }
}

var fruit = { apple: 200, orange: 300, banana: 180 }
console.log(fruit.apple)
console.log(fruit.orange)
console.log(fruit.banana)

for (let key in fruit) {
  console.log(fruit[key])
}

names.push('小野寺')
console.log(names[5])
names.unshift('カビゴン')
console.log(names[0])

var names1 = ['佐藤', '佐々木']
var names2 = ['高橋', ...names1, '鈴木', '小松']
console.log(names2[4])

names.shift()
console.log(names[0])

names.pop()
console.log(names[5])

var sports = ['野球', 'バスケットボール', 'サッカー']
for (let sport of sports) {
  console.log(sport)
}

array2D = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 0],
]
for (let array1D of array2D) {
  for (let val of array1D) {
    console.log(val)
  }
}

sports.push('バレーボール')
console.log(sports[3])

sports.shift(sports)
console.log(sports[0])
