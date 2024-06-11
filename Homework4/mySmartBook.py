import datetime

my_money_book = {
    '점심': ('2022년 6월 8일 10시 30분', '지출', '외식', 10000, '파스타 신용카드 사용')
}

def my_date():
    return datetime.datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분')

def income():
    entry = input("수입을 입력해 주세요 (예: 월급 월급 2000000 까페알바) >> ")
    item, group, amount, *memo = entry.split()
    memo = " ".join(memo) if memo else '.'
    my_money_book[item] = (my_date(), '수입', group, int(amount), memo)

def expense():
    entry = input("지출을 입력해 주세요 (예: 저녁 외식 30000 중국집) >> ")
    item, group, amount, *memo = entry.split()
    memo = " ".join(memo) if memo else '.'
    my_money_book[item] = (my_date(), '지출', group, int(amount), memo)

def show():
    total_income = 0
    total_expense = 0
    for item, details in my_money_book.items():
        date, trans_type, group, amount, memo = details
        print(f"{date} - {item}: [{trans_type}] 그룹={group}, 금액={amount}원, 메모={memo}")
        if trans_type == '수입':
            total_income += amount
        elif trans_type == '지출':
            total_expense += amount
    print(f"총수입 {total_income}원, 총지출 {total_expense}원 수입-지출={total_income - total_expense}원")

def calc():
    expression = input("계산식을 입력하세요 (예: 2000*(3000+25000)/100) >> ")
    result = eval(expression)
    print(f"계산 결과는 {result} 입니다")
    memo = f"{expression} = {result}"
    my_money_book['계산기'] = (my_date(), '계산기', '계산기', 0, memo)
