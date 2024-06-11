import random

winnum = set()

def buyautolotto():
    lotto = []
    for _ in range(5):
        numbers = set()
        while len(numbers) < 6:
            numbers.add(random.randint(1, 45))
        lotto.append(numbers)
    return lotto

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

