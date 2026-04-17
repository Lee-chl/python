max_value = max(1,30,50)
print(max_value)

min_value = min(1,30,50)
print(min_value)

max_str = max('AAC','ABC','ACC')
print(max_str)

min_str = min('AAC','ABC','ACC')
print(min_str)

length = len("hihi")
print(length)

result = eval("10+20+30+40") # 바로 실행되게 하는 함수 
print(result)

result = eval("not 40<50")
print(result)

list=[2,5,5,3,9,1]
result = sorted(list)
print(result)

str1 ="hihi"
str_id = id(str1)
print(str_id)

list_id = id([1,2,3,4,5])
print(hex(list_id)) # 16진수
print(oct(list_id)) # 8진수
print(type(list_id)) # 타입 알려주는 함수
print(type(3.14))
print(abs(-5)) # 절대값