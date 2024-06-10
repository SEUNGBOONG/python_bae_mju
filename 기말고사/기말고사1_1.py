import ftn

my_id = 0
login = False
while (True):

    cmd = input("ABC 수영클럽(1=로그인 2=회원가입 3=일정 4=회비 0=종료)")

    if (login == False and (cmd == '3' or cmd == '4')):
        print("먼저 로그인을 해주세요")
    elif (cmd == '1'):
        my_id = ftn.login()
        login = True
    elif (cmd == '2'):
        my_id = ftn.register()
        login = True
    elif (login == True and cmd == '3'):
        ftn.schedule(my_id)
    elif (login == True and cmd == '4'):
        ftn.payment(my_id)
    elif (cmd == '0'):
        break
    print()
