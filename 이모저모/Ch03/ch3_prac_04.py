# ch3 실습문제 종합

my_memo = ['운동하기', '영화 보기', '쇼핑하기']

print('파이썬 중간고사 제 이름은 홍길동 학번은 123456 입니다')
while True:
    print('='*20)
    command = input('명령을 입력하세요>> ')
    c_list = command.split(' ')
    if command == '종료':
        break
    elif command == '전체 출력':
        for n in my_memo:
            print(n)
    elif c_list[:2] == ['메모', '추가']:
        my_memo.append(command[6:])
        print(my_memo)
    elif c_list[0] == '메모' and c_list[2] == '보여줘':
        if c_list[1][-1] == '번':
            if c_list[1][:-1].isdigit():
                num = int(c_list[1][:-1])
                print(my_memo[num])
    elif c_list[0] == '메모' and c_list[2] == '삭제':
        if c_list[1][-1] == '번':
            if c_list[1][:-1].isdigit():
                num = int(c_list[1][:-1])
                my_memo.remove(my_memo[num])
                print(my_memo)

print('프로그램을 종료합니다')
