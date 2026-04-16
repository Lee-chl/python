age = input('나이를 입력하시오')
print(age)
num = 3

diff = input('변화량을 입력하시오')
#print(num + diff) # 에러 text가 넘어오기 때문!
print(num + int(diff)) # 이렇게 int() 해서 str형을 int로 바꿔줘야한다.