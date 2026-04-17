try:
    with open('test11.txt','r')as f:
        f.readlines()
except:
    print('여는 동안 에러 발생 ')
