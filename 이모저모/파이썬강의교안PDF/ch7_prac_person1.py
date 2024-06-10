# 클래스 간단한 실습

class Person:
    name = "홍길동"
    age = 20

    def speak(self):
        print(f"내 이름은 {self.name} 나이는 {self.age}살입니다.")


p1 = Person()
p1.speak()
