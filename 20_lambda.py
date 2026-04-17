def add(x,y):
    return x+y

f= lambda x,y: x+y

print(add(1,2))
print(f(1,2))

# lambda if 문 
f = lambda x: x if x % 3 == 0 else 0 # if문이 true면 앞에 x false면 else 
print(f(3))
print(f(4))

# map 함수 람다
nums = [1, 2, 3, 4, 5, 6, 7]
def pow(x):
    return x ** 2
f = lambda x:x**2
print(list(map(pow,nums))) # 출력을 위해 list로 만들어서 출력 
print(list(map(f,nums)))
print(list(map(lambda x:x**2,nums))) # map()은 전역 함수라서 맨 뒤에 넘겨줄 대상 적어야한다.

num1 = [1,2,3,4,5]
num2 =[6,7,8,9,10]
print(list(map(lambda x,y:x*y,num1,num2))) # 각 리스트에서 하나씩 나와 곱해진 수들의 리스트 만들어짐

#map과 lambda를 이용해서 1~10 list의 각 아이템에 5배를 가진 list를 만들고 출력하시오.
list1 = list(range(1,11))
print(list(map(lambda x:x*5,list1)))

# filter
ages = [18,19,39,12,43,13,21,25]

def adult_func(age):
    if age >= 19:
        return True
    else:
        return False
    
for age in filter(adult_func,ages):
    print(age)
print()

for age in filter(lambda age:age >=19,ages):
    print(age)

adult_age = list(filter(lambda age:age>=19,ages))
print(adult_age)

#1부터 10 사이의 정수를 가진 리스트에서 짝수만 나오게 필터링한 결과 리스트의 모든 원소에 대해 제곱을 수행해서 리
#스트로 반환하는 코드를 필터와 맵과 람다를 이용해서 작성하시오.
list2 = list(range(1,11))
even_num = list(filter(lambda num:num%2==0,list2))
print(list(map(lambda num:num **2,even_num)))

# reduce()
from functools import reduce # import 해서 사용 

nums = [1,2,3,4]
sum = reduce(lambda x,y:x+y,nums)
print(sum)

mul = reduce(lambda x,y:x*y,nums)
print(mul)

list3 = list(range(1,11))
result = reduce(lambda x,y: x * y,
                     filter(lambda num : num % 2 == 0,list3))
print(result)

# list 축약표현
list1 = list(range(1,11))

list2 = list(map(lambda x:x**2,list1))
print(list2)

list3 = [x**2 for x in list1] # 축약표현
print(list3)

list4 = [x**2 for x in range(1,11)] # 축약표현
print(list4)

# filter 붙여서 사용 하기 

list1 = list(range(1,11))
# 조건문에 따라 5보다 큰 값만
list5 = [x**2 for x in list1 if x>5]
print(list5)

# 조건문에 따라 짝수 값만
list6 = [x**2 for x in range(1,11) if x % 2 == 0]
print(list6)

# quiz
# 1~10까지 숫자의 제곱을 포함하는 리스트
list7 = [x**2 for x in range(1,11)]
print(list7)
# 1~20까지의 짝수를 포함하는 리스트
list8 = [x for x in range(1,21) if x % 2 ==0]
print(list8)
# 1~20까지의 숫자중 3의 배수를 포함하는 리스트
list9 = [x for x in range(1,21) if x % 3 == 0]
print(list9)
# 1~20까지의 숫자중 5의 배수의 제곱을 포함하는 리스트
list10 =[x**2 for x in range(1,21) if x % 5 == 0]
print(list10)
