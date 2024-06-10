#60181958 허찬영

printer_list = [['잉크젯', 200, 100], ['레이저젯', 200, 100], ['Epson', 200, 100]]
money = 200000
print("파이썬 중간고사 제 이름은 허찬영 학번은 60181958 입니다")
print('='*50)

while True:
    order = int(input('명령을 입력하세요 (1=사용 2=상태 3=보충 4=종료) >> '))
    if order == 1:
        printer,paper = input('프린터와 장수를 입력하세요 (예: 잉크젯 20) >> ').split()
        paper = int(paper)
        for x in range(3):
            if printer == printer_list[x][0]:
                printer_list[x][1] -= paper
                printer_list[x][2] -= int(paper/10)
            elif printer == printer_list[x][0]:
                printer_list[x][1] -= paper
                printer_list[x][2] -= int(paper/10)
            elif printer == printer_list[x][0]:
                printer_list[x][1] -= paper
                printer_list[x][2] -= int(paper/10)
                
    elif order == 2:
        for i in range(3):
            j=0
            print(printer_list[i][j],'종이',printer_list[i][j+1],'토너',printer_list[i][j+2])
        print(money)
            
    elif order == 3:
        supply_printer,supply_paper,supply_toner = input('보충 프린터와 장수와 토너수를 입력하세요 (예: 잉크젯 100 50) >> ').split()
        supply_paper = int(supply_paper)
        supply_toner = int(supply_toner)
        for y in range(3):
            if supply_printer == printer_list[y][0]:
                printer_list[y][1] += supply_paper
                printer_list[y][2] += supply_toner
                money -= supply_paper * 100 + supply_toner * 200
            elif supply_printer == printer_list[y][0]:
                printer_list[y][1] += supply_paper
                printer_list[y][2] += supply_toner
                money -= supply_paper * 100 + supply_toner * 200
            elif supply_printer == printer_list[y][0]:
                printer_list[y][1] += supply_paper
                printer_list[y][2] += supply_toner
                money -= supply_paper * 100 + supply_toner * 200

    elif order == 4:
        print('프로그램을 종료합니다')
        break
    else:
        print('잘못된 명령입니다')
        

