def gcd(a,b):
    while b!=0:   # a를 b 로 나눈 나머지가 0이 아닐 동안 시행(0이면, 최대공약수를 구한 것이므로)
        r = a % b   # a를 b 로 나눈 나머지
        a = b   # 계산 후에는, a 에 b 를 넘겨주고
        b= r   # b 자리에는, 얻은 나머지를 넘겨준다
    return a


a, b = map(int,input().split())
if a>=b:   # a 가 작은 값, b 가 큰 값
    k=gcd(a,b)
else:
    a,b = b,a
    k=gcd(a,b)

print(k)
print(a*b//k)



