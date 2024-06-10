# 클래스와 상속 간단한 실습

class Person:
    name = "홍길동"
    age = 20

    def speak(self):
        print(f"내 이름은 {self.name} 나이는 {self.age}살 입니다.")


class Student(Person):
    sid = 123456

    def study(self):
        print(f"나의 학번은 {self.sid} 입니다.")


class Teacher(Person):
    subject = "math"

    def teach(self):
        print(f"나는 {self.subject}을 강의합니다.")


student1 = Student()
student1.name, student1.sid = "김영희", 60231289
student1.speak()
student1.study()
print()

teacher1 = Teacher()
teacher1.subject, teacher1.age = "파이썬", 40
teacher1.speak()
teacher1.teach()
