nationallanguage = int(input('国語の点数を入力してください >> '))
math = int(input('算数の点数を入力してください >> '))
science = int(input('理科の点数を入力してください >> '))
society = int(input('社会の点数を入力してください >> '))
english = int(input('英語の点数を入力してください >> '))
scores = [nationallanguage, math, science, society, english]

print(f'合計点は{sum(scores)}点です')
print(f'平均点は{sum(scores) / len(scores)}点です')

hobbies = {
    'A': {'運動', '音楽', '読書', '映画鑑賞', '男漁り'},
    'B': {'運動', '悪口', '料理', 'ドライブ', '音楽'}
}
input('心の準備が出来たらenterキーを押してください')
seki = hobbies['A'] & hobbies['B']
wa = hobbies['A'] | hobbies['B']
print(len(seki) / len(wa) * 100)