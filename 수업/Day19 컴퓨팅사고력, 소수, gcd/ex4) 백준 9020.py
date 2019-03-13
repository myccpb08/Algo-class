import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    # 소수 표시
    p = [1] * (n + 1)
    for i in range(2, n + 1):
        if i*i > n:
            break
        if p[i] == 1:
            p[2 * i::i] = [0] * ((n // i) - 1)

    # 값 찾기
    a = n//2
    while p[a]==0 or p[n-a]==0:   # 둘 중 하나라도 합성수이면 계속 반복
        a -= 1

    print(a, n-a)