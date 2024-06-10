#이승엽 60215276
menu_list=['아메리카노','카페라떼']
price_list=[4000,5000]
order_list=[0.0]
money=0

print("파이썬 중가고사 제 이름은 이승엽 학번은 60215276 입니다.")
print("=" * 50)
str=()
while str != "종료":
    str = input("카페 명령을 입력하세요 >>")
    print("=" * 50)
    if str =="명령 보기":
        print("명령 보기, 메뉴 보기, 메뉴 추가, 메뉴 삭제, 주문 추가, 주문 내역, 주문초기화, 종료")
    elif str =="메뉴 보기":
            print("메뉴 %s 가격 %d 원"%(menu_list[0],price_list[0]))
            print("메뉴 %s 가격 %d 원"%(menu_list[1],price_list[1]))
            #수정

    elif str[0:5] =="메뉴 추가":
        if not str[10:]:
            print("추가할 내용이 없습니다.")
        else:
            menu_add=str[6:10]
            menu_list.append(menu_add)
            price_add=int(str[11:])
            price_list.append(price_add)
            order_list.append(0)
            print("%s %d원 추가 되었습니다."%(menu_add,price_add))

    elif str[0:5] == "메뉴 삭제":
        if str[6:]==menu_list[0]:
            pop_menu=menu_list[0]
            print("메뉴 %s가 삭제되었습니다."%menu_list[0])
            menu_list.pop(0)
            price_list.pop(0)


        elif str[6:]==menu_list[1]:
            pop_menu=menu_list[1]
            print("메뉴 %s가 삭제되었습니다."%menu_list[1])
            menu_list.pop(1)
            price_list.pop(1)

        elif str[6:] == menu_list[2]:
            pop_menu = menu_list[2]
            print("메뉴 %s가 삭제되었습니다."%menu_list[2])
            menu_list.pop(2)
            price_list.pop(2)


    elif str[0:5]=="주문 추가":
        if str[6:11] == menu_list[0]:
            jumun = str[6:11]
            tnfid=int(str[12])
            order_list[0]=tnfid
            money+=(tnfid*price_list[0])
            print("메뉴 %s 총 %d 개 주문 되었습니다."%(menu_list[0],order_list[0]))
            if str =="주문 내역":
                print("메뉴 %s 가격 %d원 수량 %d" % (menu_list[0], price_list[0], order_list[0]))
                print("메뉴 %s 가격 %d원 수량 %d" % (menu_list[1], price_list[1], order_list[1]))

                print("총 주문액은 %d원 입니다. " % money)




        elif str[6:10] == menu_list[1] :
            jumun=str[6:10]
            tnfid=int(str[11])
            order_list[1]=tnfid
            money+=(tnfid*price_list[1])
            print("메뉴 %s 총 %d 개 주문 되었습니다."%(menu_list[1],order_list[1]))

        elif str[6:10] == menu_list[2]:
            jumun = str[6:10]
            tnfid = int(str[11])
            order_list.append(tnfid)
            money+=(tnfid*price_list[2])

            print("메뉴 %s 총 %d 개 주문 되었습니다."%(menu_list[2],order_list[2]))


    elif str[0:6]=="주문 초기화":
        print("주문이 초기화 되었습니다.")
        order_list.clear()

    elif str[0:2]=="종료":
        print("프로그램을 종료합니다.")
        break

    #수정하자
    elif str=="주문 내역":
        if not order_list==0:
            print("주문 내용이 없습니다.")



    else:
        print("잘못된 명령어 입니다.")

