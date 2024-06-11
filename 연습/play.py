import ftn

my_id = 0
login = False
while(True):

    cmd =input("ABC 수영클럽(1=로그인 2=회원강비 3= 일정 4= 회비 0= 종료)")
    if(login == False and (cmd =='3' or cmd =='4')):
        print("먼저 로그인을 해주세요")
    elif (cmd =='1'):
        my_id = ftn.login()
        login==True

    elif (cmd =='2'):
        my_id=ftn.register()
        login=True
    elif (cmd =='3'):
        ftn.schedule(my_id)
    elif (cmd =='4'):
        ftn.payment()
    elif (cmd =='0'):
        break
    print()