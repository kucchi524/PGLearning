function triangle(width, height) {
  return (width * height) / 2
}

var triangle2D = [
  [5, 2],
  [10, 6],
  [4, 7],
]
for (let i = 0; i < 3; i++) {
  var width = triangle2D[i][0]
  var height = triangle2D[i][1]
  var result = triangle(width, height)
  console.log('%dつ目の三角形の面積：%d', i + 1, result)
}

var v_outHensu = 'varで宣言した関数外の変数'
let l_outHensu = 'letで宣言した関数外の変数'
outHensu = '関数外の変数'
function output() {
  console.log('・・・output()開始・・・')
  var v_inHensu = 'varで宣言した関数内の変数'
  let l_inHensu = 'letで宣言した関数内の変数'
  inHensu = '関数内の変数'
  console.log('--- 関数外で宣言された変数を表示します ---')
  console.log(v_outHensu)
  console.log(l_outHensu)
  console.log(outHensu)
  console.log('--- 関数内で宣言された変数を表示します ---')
  console.log(v_inHensu)
  console.log(l_inHensu)
  console.log(inHensu)
  console.log('・・・output()開始・・・')
}
output()
console.log('--- 関数外で宣言された変数を表示します ---')
console.log(v_outHensu)
console.log(l_outHensu)
console.log(outHensu)
/* console.log('--- 関数内で宣言された変数を表示します ---')
console.log(v_inHensu)
console.log(l_inHensu)
console.log(inHensu)
console.log('・・・output()開始・・・') */

function output2() {
  var hensu
  console.log(hensu)
  hensu = '変数'
}
output2()

var output2 = function () {
  console.log('関数学習中')
}
for (let i = 0; i < 3; i++) {
  output2()
}

var triangle = function (width, height) {
  return (width * height) / 2
}

var triangle2D = [
  [5, 2],
  [10, 6],
  [4, 7],
]
for (let i = 0; i < 3; i++) {
  var width = triangle2D[i][0]
  var height = triangle2D[i][1]
  var result = triangle(width, height)
  console.log('%dつ目の三角形の面積：%d', i + 1, result)
}

var result = (function (width, height) {
  return (width * height) / 2
})(10, 8)
console.log('三角形の面積: %d', triangle)

var outFunction = function () {
  var num = 1
  return function () {
    console.log(num)
    num = num + 10
  }
}
var callFunction = outFunction()
for (let i = 0; i < 3; i++) {
  callFunction()
}

function tax(price) {
  return price * 1.1
}
console.log(tax(100))
console.log(tax(500))
console.log(tax(1500))

var daikei = function (joutei, katei, height) {
  return ((joutei + katei) * height) / 2
}
console.log(daikei(10, 8, 4))
