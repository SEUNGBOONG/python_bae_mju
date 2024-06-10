# section_069 매개변수 기본값

def report(message, job, who='Everyone', message2='Good bye!'):
    print(message, job, who, message2)

report('Good morning', 'worker', 'Have a good day!')  # 사실 message2 만 전달하길 원했음
report('Good morning', 'student', 'Mr. Park', 'Have a good day!')
report('Good morning', 'worker', message2='Have a good day!')  # message2 만 전달. 키워드 인수.
report('Good morning', 'student', message2='Have a good day!', who='Mr. Park')  # 키워드 인수 순서 무관
print()

# section_070 가변인수

def select_even_odd(msg, *arg):
    result = [msg]
    for num in arg:
        if msg == 'even':
            if num%2 == 0:
                result.append(num)
        else: # odd
            if num%2 == 1:
                result.append(num)
    return result

print(select_even_odd('odd', 1,2,3,4))
print(select_even_odd('even', -12, 2, 81, 99, 48, 20))
print()

# section_070 키워드 가변인수

def my_book_report(**kwargs):
    total = 0
    print('가계부 내역 출력:')
    for key in kwargs.keys():
        print(f'항목 {key}: 금액 {kwargs[key]}원')
        total += kwargs[key]
    else:
        print(f'총액은 {total}원입니다')

my_book_report(점심=10000, 커피=3000, 저녁=12000)

my_dict = {'점심': 10000, '커피': 3000, '저녁': 12000}
my_book_report(**my_dict)

