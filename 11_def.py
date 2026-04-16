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