# 자식이 있으면, 자기는 연산자
# 자식이 없으면, 자기는 숫자

for i in range(1,11):
    n=int(input())
    flag=1
    for j in range(n):
        info=input().split()
        if len(info)>2:   # 자식이 있다는 의미
            if not info[1] in ['-','+','*','/']:
                flag=0
        else:
            if info[1] in ['-','+','*','/']:
                flag=0
    print('#{} {}'.format(i,flag))