for i in range(1,987654321):
    n = int(input())
    if n==0:
        break
    else:  # n초과, 2n 이하의 소수 개수를 출력
        notprime = [0]*(2*n+1)
        notprime[0] = notprime[1] = 1  # 0과 1은 소수가 아니므로 1로 바꿈

        a = int((2*n) ** (1 / 2))  # 루트 n 까지만 하면 되므로

        for i in range(2, a + 1):
            k = 2
            while i * k <= 2*n:
                notprime[i * k] = 1  # 배수는 1로 바꿈
                k += 1

        count = 0
        for i in range(n+1, 2*n+1):
            if notprime[i] == 0:
                count += 1

        print(count)
