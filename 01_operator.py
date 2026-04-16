print(5**3)
print(20%3)
print(4*2)
print(1/2)
print(5//3)  #나눗셈 몫 
# type check
print(type(1.1))
print(type('Hello'))
# 대입 연산자
num = 3
num *=3;
print(num)
# 비교 연산자
print('Hello' > 'World!')
print( 5 < 6)
result = 13 ==4
print(result)

# 비교 논리 연산자 실습
print(True and True)
print(True or False)
print(5<6 and True)
num1 = 3
num2 = 5
print(not(num1>num2))

# print 함수
print('hi')
name = 'hoho'
age = 20
print('내이름은 ' + name+ ' 나이는 '+ str(age));

# string fomat()
str1 = "{}".format(10)
print(str1)

str2 = "{}과 {}".format(10,20)
print(str2)

num1 = 10
num2 = 20
str3 = "{}x{}={}".format(num1,num2,num1*num2)
print(str3)
# 순서 (아무것도 안 넣으면 순서대로)
str5 = '두번째부터 {1} 그 다음 첫번째 {0} '.format(num1,num2)
print(str5)
str6 = '첫번째부터 {0} 그 다음 두번째 {1}'.format(num1,num2)
print(str6)

# 데이터 타입 넣어서 포맷팅
str7 = '이름 {:s} 나이는 {d}'.format(name,age)
print(str7)
print('pi = {:f}'.format(3.141592))
print('pi = {:10f}'.format(3.141592))  #10자리 
print('pi = {:5.2f}'.format(3.141592)) # 정수는 5자리 점 뒤는 2
print('pi = {:.2f}'.format(3.141592)) # 소숫점 뒷자리 2
# 서식 지정자
print('이름은 %s 나이는 %d'%{name,age})
print('이름은 %s 나이는 %5d'%{name,age}) # 5자리고 앞이 비면 공백
print('이름은 $s 나이는 %05d'%(name,age)) # 5자리고 앞이 비면 0 
print('pi = %f'%3.141592)
print('pi = %5.2f'%3.141592)
print('pi = %.2f'%3.141592)