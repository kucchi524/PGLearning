def welcome(u):
    print(f'ようこそ{u["name"]}さん')
    u['age'] = u['age'] + 1
    print(f'あなたは来年{u['age']}歳だから大吉です')

user_name = input('名前を入力してください >>')
user_age = int(input('年齢を入力してください >>'))
user_info = [user_name, user_age]
user = {'name': user_name, 'age': user_age}
welcome(user)
print(f'{user_info[1]}歳の{user_info[0]}さん、またプレイして下さい')