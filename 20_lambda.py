def add(x,y):
    return x+y

f= lambda x,y: x+y

print(add(1,2))
print(f(1,2))

# lambda if 문 
f = lambda x: x if x % 3 == 0 else 0
print(f(3))
print(f(4))