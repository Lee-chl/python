def hello():
    print('hi')
hello()

# 가변 매개변수가 있는 함수 *를 사용 
def hello1(greeting,*names):
    for name in names:
        print(greeting,name)

hello1("hi","me","you","are","ho","ha")

# 함수 호출 시 매개변수 명 사용 
def function(first,second,third):
    return first + second + third

print(function(3,5,7))
print(function(first=3,second=5,third=7))
print(function(second=5,third=7,first=3))

# 매개변수 기본값
def function1(first=1,second=3,third=5):
    return first + second +third
print(function1())
print(function1(second=5))
print(function1(1,2))

# 기본값 없을땐 무조건 써줘야한다. 
def function2(first,second,third=1):
    return first+second+third
print(function2(1,2,3))
print(function2(1,2))
print(function2(first=2,second=1))
print(function2(1,second=2))
print(function2(second=2,first=1))

# 반환형이 콜렉션일 떄 unpacking
def function3():
    return 1, "Hello",True
a, b, c = function3()
print(a,b,c)
print(type(a))
a= function3()
print(type(a))
print(a)

# list 반환시 
def ret_list():
    return [1,2]
l = ret_list()
print(l)

n1 , n2 = ret_list()
print(n1,n2)

n1, _ = ret_list()
print(n1)