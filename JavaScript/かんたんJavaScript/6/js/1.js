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
