import random

list1 = list(range(1,46))
random.shuffle(list1)
result = list1[0:6]
result.sort()
print(result)

# sample 사용해서 더 쉽게 
list1 = list(range(1,46))
result = random.sample(list1,6)
result.sort()
print(result)
