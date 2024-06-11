import mySmartBook as mlt

print("홍길동(학번 123456)의 스마트 가계부에 오신 것을 환영합니다")

while True:
    command = input("명령 입력: 1=수입 2=지출 3=출력 4=계산기 q=종료 >> ").strip()
    if command == '1':
        mlt.income()
    elif command == '2':
        mlt.expense()
    elif command == '3':
        mlt.show()
    elif command == '4':
        mlt.calc()
    elif command.lower() == 'q':
        print("이용해 주셔서 감사합니다")
        break
    else:
        print("잘못된 명령입니다. 다시 입력해 주세요.")
