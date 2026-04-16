for i in range(10):
    print('HI!')

for i in range(1,10):
    print('Hi! ',i)

for i in range(10,0,-1):
    print(i)

# list tuple for in문
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
fruits = ('Apple','Mango','Banana')
for fruit in fruits:
    print(fruit)
tuple1 = (1,2,3,4,5,6,7,8,9,10)
for num in tuple1:
    print(num)

# input 함수 이용해 입력받은 횟수만큼 반복 
str_count = input('반복할 횟수 입력해주세요')
count = int(str_count)

for i in range(count):
    print('Hi! ',i)

# for 중첩
for i in range(10):
    for fruit in fruits:
        print(i,fruit)