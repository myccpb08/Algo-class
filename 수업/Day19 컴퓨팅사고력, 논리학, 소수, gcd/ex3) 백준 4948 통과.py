for i in range(1,987654321):
    n = int(input())
    if n==0:
        break
    else:
        p = [1] * (2*n + 1)
        for i in range(2, 2*n + 1):
            if p[i] == 1:
                if i * i <= 2*n:
                    p[2 * i::i] = [0] * ((2*n // i) - 1)
                else:
                    break
        print(sum(p[n+1:2*n+1]))