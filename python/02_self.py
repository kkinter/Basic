class Person:

    # 사람이라면 이름을 가지고 있다.
    # 인스턴스를 만들 때는 이름 정보를 받아서 하고 싶다.
    # 생성자 메서드  
    def __init__(self, name): # > self, name을 받아서 쓰고 싶다
        # 개별 인스턴스에 각각 name 속성을 지정
        self.name = name
    
    def greeting(self):
        print(f'안녕하세요 {self.name} 입니다. ') #개별 인스턴스의 속성으로 쓰고 싶다
    
    def one_line(self):
        return self.name[0]  # 왜 None 이 반환되는지 ?

# 인스턴스 만들떄
jimin = Person('jimin')
print(jimin.name)
print(jimin.greeting())
print(jimin.one_line())

iu = Person('iu')
print(iu.name)
print(iu.greeting())
print(iu.one_line())