# 거듭제곱 구하기

def power3(a,b):  # O(logn)  : a^b 승 구하는 거
    ans = 1
    while b > 0 :
        if b%2==1:  # b가 홀수이면
            ans *= a  # 자기 자신 한 번 미리 곱해두고
        a = a*a
        b //= 2
    return ans

print(power3(2,5))

def power2(a,b):  # O(logn)
    if b==0:
        return 1  # a^0=1
    elif b==1:
        return a   # a^1=a

    elif b&1: # b가 홀수이면
        return a*power2(a,b-1)
    else:
        temp = power2(a, b//2)
        return temp*temp