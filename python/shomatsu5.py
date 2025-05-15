def is_leapyear():
    year = int(input('年を西暦で入力してください >>'))
    if (year % 400 == 0) :
        print(f'西暦{year}年は、うるう年です。')
    elif (year % 4 == 0 and year % 100 != 0) :
        print(f'西暦{year}年は、うるう年です。')
    else:
        print(f'西暦{year}年は、うるう年ではありません。')

is_leapyear()

def int_input(msg):
    return int(input(f'{msg}を入力してください >>'))
    
def calc_payment(amount, people=2):
    dnum = amount / people
    pay = dnum // 100 * 100
    
    if dnum > pay:
        pay = int(pay + 100)
    
    payorg = amount - pay * (people - 1)
    
    return [int(pay), int(payorg)]

def show_payment(pay, payorg, people):
    print('支払額')
    print(f'1人あたり{pay}円({people}人)、幹事は{payorg}円です')
    
amount = int_input('支払総額')
people = int_input('参加人数')
[pay, payorg] = calc_payment(amount, people)
show_payment(pay, payorg, people)
