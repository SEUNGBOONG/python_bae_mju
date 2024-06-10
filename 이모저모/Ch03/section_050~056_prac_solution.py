# 실습문제 3장

# Sec 50 ~ 53

print("Sec 50~53 실습", "="*30)

input_string = input("두 개의 정수를 입력하세요: ")
num1, num2 = input_string.split()

operator = input("원하는 연산이 덧셈인지 뺄셈인지 입력하세요: ")

if operator == "덧셈" :
    print(num1,"+",num2,"=",int(num1)+int(num2),"입니다")

if operator == "뺄셈" :
    print(num1,"-",num2,"=",int(num1)-int(num2),"입니다")

if operator != "덧셈" and operator != "뺄셈" :
    print("입력이 잘못 되었습니다.")


# Sec 54 ~ 56

print("\nSec 54~56 실습", "="*30)

id_list = ['홍길동', '김영희', '파이썬']

my_id = input("사용자 아이디를 입력하세요: ")

if my_id in id_list :
    credits, gpa = input("이수한 학점수와 평점을 입력하세요: ").split()
    credits, gpa = float(credits), float(gpa)
    if credits >= 140 and gpa >= 4.0 :
        print("우등 졸업이 가능합니다")
    elif credits >= 140 and 2.5 <= gpa < 4.0 :
        print("졸업이 가능합니다")
    else:
        print("졸업이 불가능합니다.")
else :
    print("등록된 사용자가 아닙니다.")
