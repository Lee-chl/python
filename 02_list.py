scores = [30,50,90,89,56,87]
score0 = scores[0]
print(score0)
print(scores[5])
print(scores[0])
print(scores[-1])
print(scores[-3])

# 수정
scores[1] = 100
print(scores)
# 추가
scores.append(99)
scores.append('Hello')
# 특정 위치에 삽입 
scores.insert(1,33)
print(scores)
scores.insert(2,'World')
print(scores)

# + 와 * 연산자 사용 가능 
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9,10]
print(list1 + list2) 
print(list2 + list1)
print(list1 * 3) # list1 내용 세번 반복
print(list2 * 3) # list2 내용 세번 반복