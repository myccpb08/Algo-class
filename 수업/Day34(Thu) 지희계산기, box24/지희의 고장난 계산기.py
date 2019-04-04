import sys
sys.stdin = open('계산기.txt','r')

def check(n):
    cnt = 0
    while n>0:
        if btn[n%10]==0:  # 해당버튼 사용불가
            return 987654321
        else:
            cnt+=1
            n=n//10
    return cnt

for t in range(int(input())):
    print('#{}'.format(t+1),end=' ')
    btn=list(map(int,input().split()))
    x= int(input())

    if x==1 and btn[1]==0:
        print(-1)
        continue

    a=check(x)
    if a < 97654321:   # 현재버튼으로 바로 x 를 만들 수 있으면
        print(a+1)  # 버튼누르고 계산버튼 추가
    else:
    # 약수찾기
        aliquot=[]
        i=2
        while i**2<x:
            if x%i==0:   # 약수이면
                a = check(i)
                b = check(x//i)
                if a < 987654321:
                    aliquot += [(i, a)]
                if b < 987654321:
                    aliquot += [(x//i, b)]
            i+=1

        aliquot.sort(key=lambda x:x[0],reverse=True)

        flag = 0
        while True:
            if x==1:
                print(answer)
                break
            if x>1 and flag==1:
                print(-1)
                break
            answer = 0
            for div in aliquot:
                while x%div[0]==0:   # 나누어 떨어지면
                    answer += (div[1]+1)
                    x= x//div[0]

            flag = 1
