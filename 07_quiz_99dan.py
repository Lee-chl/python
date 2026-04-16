dan_str = input('몇단을 출력할까요?')
dan = int(dan_str)

for i in range(1,10):
    print('{} X {} = {}'.format(dan,i,dan * i))