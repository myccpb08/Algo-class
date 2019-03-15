kinds_coin , wallet = map(int,input().split())  # 동전종류3, 만들 돈 10

value = [ int(input()) for i in range(kinds_coin)]  # 동전종류 1, 2, 5

# 식은 d(n) = d(n) + d(n-k)  : n 만들고 싶을 때,    k = 추가된 동전의 가치,    n=wallet 이고, k 는 value 의 인덱스로 바뀜
# 동전이 추가된 뒤의 경우의수 d(n) = [추가되기 전에 n만들 때의 경우의수 d(n)] + [추가된 후에 d(n-k) ]

memo = {}
# 할 일. 동전 0개일 때꺼 저장해야 함

def coin(kinds_coin, wallet):  # ( 동전종류수, 목표, 동전값)
    global memo, value
    note = str([kinds_coin, wallet])   # 동전 3개 썼을 때, 목표값의 경우의 수가 딕셔너리를 기록할 예정임
    if note in memo:  # 딕셔너리에 이미 기록되어 있다면
        return memo[note]  # 그 값을 리턴하면 됨

    elif kinds_coin ==0:  # 현재 사용하는 동전종류가 0이면, 돈을 만들 수 없으니 무조건 0
            return 0
    elif kinds_coin ==1:
            if wallet%value[0]==0:
                 memo[note]=1
            else:
                    memo[note]=0
            return memo[note]

    else:  # 기록되어 있지 않다면
        memo[note]=coin(kinds_coin-1, wallet) + coin(kinds_coin, wallet-value[kinds_coin-1])
        return memo[note]

print(coin(kinds_coin, wallet))