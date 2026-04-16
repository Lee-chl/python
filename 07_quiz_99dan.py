dan_str = input('몇단을 출력할까요?')
dan = int(dan_str)

for i in range(1,10):
    print('{} X {} = {}'.format(dan,i,dan * i))

# 전체 구구단 출력 
for i in range(1,10):
    print('---{}단---'.format(i))
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))