memo=[-1]*101
memo[0]=0  # 피보나치 0항
memo[1]=1  # 피보나치 1항
def fibo(n):
    global memo
    if memo[n]!=-1:   # 값이 기록되어 있으면
        return memo[n]  # 그 값을 바로 가지고 가서 써
    else:
        memo[n]=fibo(n-1)+fibo(n-2)  # 값 기록되어 있지 않으면, 계산해서 쓰고
        return memo[n]  # 그 값을 가지고 가

print(fibo(100))