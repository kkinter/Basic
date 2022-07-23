class Person:
    # 클래스 변수(속성)
    species = '사람'
    # 인스턴스 메서드
    # 인스턴스가 활용할 메서드 
    def greeting(self):
        print('hi!')

# 인스턴스가 메서드를 실행시킴
iu = Person()
iu.greeting()

print(Person().greeting())

print(Person.species)