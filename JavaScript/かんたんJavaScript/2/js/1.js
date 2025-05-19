let pen = '青いペン'
let Pen = '黄色いペン'
let PEN = '赤いペン'
console.log(Pen)

pen = 'これは"青いペン"です'
console.log(pen)

/* 変数を使ったあいさつ文作成 */
function createGreeting(name) {
  console.log(name + 'さん、こんにちは')
}

// あいさつ文を作成する
var sayHello = createGreeting('カビゴン')

// インデント
for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 5; j++) {
    var ans = i * j
    console.log(ans)
  }
}

// あいさつを表示する
console.log('こんにちは')
