student = ('hoho','인공지능학과',3,175.3,3.5,True)
print(student)
print(student[0])

# student[0] = '정국' 에러 immutable

car = ['Tesla','model3','red',500]
print(car)

# range 사용해 tuple 생성
range1 = range(10)
tuple1 = tuple(range1)
print(tuple1)
range2 = range(-5,15,2)
print(tuple(range2))