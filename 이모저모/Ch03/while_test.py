# while 문과 if 문의 연습.
#
# 가계부 프로그램 v.1.0

print('가계부 프로그램에 오신 것을 환영합니다')
print('=' * 45)
print()

cmd = input('명령을 입력하세요 (1=내역입력, 2=결과출력, 3=종료) ')

money_list = []
price_list= []
total = 0

while cmd != '3' :

    if cmd == '1' :
        item = input('지출항목을 입력하세요: ')
        money = int(input('지출금액을 입력하세요: '))
        
        money_list.append(item)
        price_list.append(money)
        total += money

    elif cmd == '2' :
        print('지출항목 리스트입니다')
        print(money_list)
        print(price_list)
        print('지출 총액은', total, '원입니다')

    else :
        print('잘못된 명령입니다')

    print()
    cmd = input('명령을 입력하세요 (1=내역입력, 2=결과출력, 3=종료) ')

print('프로그램을 종료합니다')


