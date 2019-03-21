n,m = map(int,input().split())

if n>=3:
    if m>=7:
        print(m-2)  # 4번가는 최소요건
    elif m>=4:
        print(4)
    else:
        print(m)

if n==1:  # 위 아래로 이동 불가
    print(1)

if n==2:  # 2번 3번 방법밖에 못 씀
    if m>=7:
        print(4)
    else:
        print((m+1)//2)