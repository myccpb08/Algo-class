m,n = map(int,input().split())

# 0인 것을 출력할 예정
notprime = [0]*(n+1)    # 인덱스 맞춰주기 위해 한 칸 더 만듦
notprime[0]=notprime[1] = 1  # 0과 1은 소수가 아니므로 1로 바꿈

a = int(n**(1/2))   # 루트 n 까지만 하면 되므로

for i in range(2, a+1):
    k = 2
    while i * k <=n:
        notprime[i*k] = 1  # 배수는 1로 바꿈
        k += 1

for i in range(m,n+1):
    if notprime[i]==0:
        print(i)