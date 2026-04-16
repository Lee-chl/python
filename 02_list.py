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

# len()
length = len(scores)
print('scores의 길이는 {}입니다.'.format(length))
bts = ['진','슈가','제이홉','RM','지민','정국','뷔']
print('bts 멤버는 {}명입니다.'.format(len(bts)))

# list 분할
numbers = [0,10,20,30,40,50,60,70,80,90,100]
numbers1 = numbers[0:4]
print(numbers1)
print(numbers[:4]) # 처음부터 4번째 전까지 
print(numbers[7:11])
print(numbers[7:]) # 7부터 끝까지
print(numbers[:]) # 처음부터 끝까지

# range(): 범위
r1 = range(1,10,1) # 1~9 까지 1씩 증가하는 범위
print(r1)

r2 = range(10,20,2) # 10~ 19 까지 2씩 증가하는 범위
print(r2)

r3 = range(10,0,-1) # 10~ 1 까지 -1씩 감소하는 범위
print(r3)

r4 = range(10,0,-2) # 10 ~1 까지 -2씩 감소하는 범위
print(r4)

# range 이용 해 list 생성
list1 = list(range(10))
print(list1)
list2 = list(range(1,10))
print(list2)
list3 = list(range(1,10,2))
print(list3)
list4 = list(range(10,0,-1))
print(list4)