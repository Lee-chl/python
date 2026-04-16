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

# 비공개 속성
class Person2:
    def __init__(self,name,age):
        self.name = name
        if 0 <= age <= 20 : self.__age = age ## __ 는 비공개 속성
        else: self.__age=0

    def inc_age(self):
        self.__age += 1

    def info(self):
        print(self.__age)
        
    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살입니다.'.format(self.__age))

person3 = Person2('홍길동',20)
person3.hello()
person3.inc_age()
person3.info()