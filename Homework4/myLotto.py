import random
import datetime

my_money_book = {
    '점심': ('2022년 6월 8일 10시 30분', '지출', '외식', 10000, '파스타 신용카드 사용')
}
winnum = set()

def a():
    return datetime.datetime.strftime("%Y년 %m월 %d일 %h시 %m분")

def income():
    entry = input("수입을 입력하세요: 예) 월급 월급 200000 카페알바")
    item, group, amount, *memo = entry.split()
    memo=''.join(memo) if memo else '.'
    my_money_book[item] =(a(), '수입',group,int(amount),memo)

def buyautolotto():
    lotto = []
    for _ in range(5):
        numbers = set()
        while len(numbers) < 6:
            numbers.add(random.randint(1, 45))
        lotto.append(numbers)
    return lotto

def buy():
    lotto= []
    for _ in range(5):
        number=set()
        while len(number) <6:
            number.add(random.randint(1,45))
        lotto.append(number)

def printlotto(lotto):
    for index, nums in enumerate(lotto):
        label = chr(ord('A') + index)
        print(f"{label} 자동", end=" ")
        printnums(nums)

def setwinlotto():
    global winnum
    winnum = set()
    while len(winnum) < 6:
        winnum.add(random.randint(1, 45))

def getwinner(lotto):
    for index, nums in enumerate(lotto):
        label = chr(ord('A') + index)
        matching_nums = nums & winnum
        if matching_nums:
            print(f"{label} 당첨번호 {len(matching_nums)}개:", end=" ")
            printnums(matching_nums)
        else:
            print(f"{label} 당첨번호 0개: 꽝")

def printnums(nums):
    print(" ".join(map(str, sorted(nums))))

