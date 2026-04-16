adult = 18
age = 17

if age < adult:
    print('당신은 미성년자 이네요.')
    print('당신은 입장 불가합니다.')

# if~ else 조건문
if age < adult:
    print('당신은 미성년자')
else:
    print('당신은 성인')

# if ~ elif (If문이 아니면 밑의 elif로 넘어가서 조건 확인 )
score = 90
if score >= 90:
    result= 'A'
elif score >= 80:
    result = 'B'
elif score >= 'C':
    result = 'C'
elif score >= 70:
    result = 'D'
else:
    result='F'
print(result)