# sec 67 함수

def hap(a, b):
    result = a + b
    print('두 수의 합을 구해 출력해주는 함수입니다')
    print(a, b, '의 합은 ', result, '입니다')

def cha(a, b):
    result = a - b
    print('두 수의 차를 구해 출력해주는 함수입니다')
    print(a, b, '의 차는 ', result, '입니다')

def hapcha(a, b, op):
    if op == '+':
        # result = a + b
        # print('두 수의 합을 구해 출력해주는 함수입니다')
        # print(a, b, '의 합은 ', result, '입니다')
        hap(a, b)
    elif op == '-':
        # result = a - b
        # print('두 수의 차를 구해 출력해주는 함수입니다')
        # print(a, b, '의 차는 ', result, '입니다')
        cha(a, b)
    else:
        print('정의되지 않은 연산입니다')

print()
hapcha(10, 20, '+')
hapcha(10, 20, '-')
hapcha(-87, 172, '+')
hapcha(-87, 172, '-')
hapcha(-87, 172, '*')