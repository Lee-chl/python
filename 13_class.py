class Person:
    def __init__(self):
        self.hi = 'Hello'
    def hello(self):
        print(self.hi)

person = Person()
person.hello()

person1 = Person();
person1.hello()
print(person.hi)

# 속성 정의와 초기화 
class Person1:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살 입니다.'.format(self.age))

person2 = Person1('홍길동',20)
person2.hello()