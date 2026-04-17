import datetime as dt,random,time,os # import 키워드 사용해 모듈 추가 , as 사용해 별칭 지정 가능 

today = dt.date.today()
print(today)
now = dt.datetime.now()

print(now)

print(now.year)
print(now.month)
print(now.day)

dir(dt)

know = now + dt.timedelta(hours=9) # 시간 더하기 빼기 가능하게 해주는 함수
print(know)

time_diff = know -now
print(time_diff)

from datetime import datetime, date # from 에서 import된 것들을 가져온다
xmas1 = datetime(2023, 12, 25, 0, 0, 0)
print(xmas1)
xmas2 = date(2023, 12, 15)
print(xmas2)

# time 

print(time.time())

local_time = time.localtime(time.time())
str_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time) # 날짜 형식 지정 
print(str_time)

# random 

print(random.random()) # 0~1미만의 실수 난수 발생
print(random.randrange(1,7)) # 1~6까지의 정수 난수 발생
print(random.randint(1,7)) # 1~7까지의 정수 난수 발생 

list1 = [1,2,3,4,5,6,7,8,9,10] 
random.shuffle(list1) # list의 아이템 순서를 바꿈
print(list1)
print(random.choice(list1)) # list의 아이템 중 하나를 임의로 선택
print(random.sample(list1,5)) # list의 아이템 중 5개의 아이템을 임의로 선택 

# os 
dir(os)

print(os.sep) # 경로 구분자 
cur_dir = os.getcwd() # 현재 작업 경로 
print(cur_dir)

test_dir = os.path.join(cur_dir,'test') # 경로 문자열로 생성  

print(test_dir)

print(os.path.exists(test_dir)) # 경로 유무 체크
if not os.path.exists(test_dir):
    os.mkdir(test_dir) # 디렉토리 생성
print(os.path.exists(test_dir))

with open('test.txt','r+') as f:
    text = f.readlines()
    for line in text:
        print(line,end="")

text = "hihi \n PYTHOn \n 반갑습니다."
with open('test.txt','w') as f:
    f.write(text)

texts = ['hihi','python','반갑습니다']
with open('test.txt','a') as f:
    f.writelines(texts)

# try except 
str1 = input('피젯수 입력하세요')
str2 = input('젯수 입력하세요')

try:
    num1 = int(str1)
    num2 = int(str2)
    result = num1 / num2 
except ValueError:
    print('숫자를 입력하세요')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except Exception as e: # Exception 넘겨 받는다 
    print('입력값을 확인하세요 ',e)
else:  # 예외 없을 시 실행 
    print('{} / {} = {}'.format(num1,num2,result))
finally: # 예외이건 아니건 무조건 실행
    print('처리 완료! ')