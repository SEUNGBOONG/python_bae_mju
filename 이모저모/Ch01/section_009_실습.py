# section_009.py 실습

##name = input("이름을 입력하세요: ")
##age = input("나이를 입력하세요: ")
##student_id = input("학번을 입력하세요: ")

input_string =input("이름과 나이와 학번을 입력하세요: ")
name, age, student_id = input_string.split(" ")

print("이름", name, "나이", age, "학번", student_id, "입니다")

