var gendar = '男性'
if (gendar == '男性') {
  console.log('男性です')
}

gendar = '女性'
if (gendar == '男性') {
  console.log('男性です')
} else if (gendar == '女性') {
  console.log('女性です')
} else {
  console.log('男性でも女性でもありません')
}

var yobi = 'TUE'
var msg = ''
switch (yobi) {
  case 'SUN':
    msg = '日曜日です'
    break
  case 'MON':
    msg = '月曜日です'
    break
  case 'TUE':
    msg = '火曜日です'
    break
  case 'WED':
    msg = '水曜日です'
    break
  case 'THU':
    msg = '木曜日です'
    break
  case 'FRI':
    msg = '金曜日です'
    break
  case 'SAT':
    msg = '土曜日です'
    break
}
console.log(msg)

switch (yobi) {
  case 'SUN':
    msg = '日曜日です'
    break
  case 'MON':
    msg = '月曜日です'
    break
  case 'TUE':
    msg = '火曜日です'
  case 'WED':
    msg = '水曜日です'
    break
  case 'THU':
    msg = '木曜日です'
    break
  case 'FRI':
    msg = '金曜日です'
    break
  case 'SAT':
    msg = '土曜日です'
    break
  default:
    msg = 'どの曜日にも一致しません'
    break
}
console.log(msg)

var num = 0
for (let i = 0; i < 5; i++) {
  console.log(num)
  num += 2
}

var data = [1, 2, 3, 4, 5]
for (let atai of data) {
  console.log(atai)
}

var x = 0
while (x < 20) {
  console.log('xの値: ' + x)
  x += 2
}

x = 10
do {
  console.log('xの値: ' + x)
} while (x < 10)

x = 0
for (let i = 1; i <= 9; i++) {
  for (let j = 1; j <= 9; j++) {
    console.log(i + '×' + j + '=' + i * j)
    if (j == 5) {
      break
    }
  }
}

x = 0
for (let i = 1; i <= 9; i++) {
  for (let j = 1; j <= 9; j++) {
    if (j == 5) {
      continue
    }
    console.log(i + '×' + j + '=' + i * j)
  }
}

x = -3
try {
  if (x < 0) {
    throw 'x に負の値が代入されています。'
  }
  console.log('xの値は' + x + 'です')
} catch (e) {
  console.log(e)
} finally {
  console.log('処理が完了しました')
}

x = 0
if (x == 0) {
  console.log('ゼロです')
} else if (x < 0) {
  console.log('マイナスです')
} else {
  console.log('プラスです')
}

for (let i = 1; i <= 10; i++) {
  for (let j = 1; j <= 10; j++) {
    console.log(i + j)
  }
}

while (x < 10) {
  console.log(x)
  x++
}
