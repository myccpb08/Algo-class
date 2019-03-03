import sys
sys.stdin = open('준혁이 여자친구.txt', 'r')

n,m = map(int,input().split())

info = [ [0]*(n+1) for i in range(n+1)]


for i in range(m):
    start, end, weight = map(int,input().split())
    info[start][end]=weight
    info[end][start]=weight


init_sum = 200*(n-1)    # 초기 최솟값 설정
sofar = 0  # 가중치 더하기 전에는 0으로 함수로 들어감

## 함수만들기

def dfs(y, sofar):
    global init_sum

    if sofar >= init_sum:  # 하다가 중간값이 설정해둔 최종값보다 커버리면 더 할 필요 x
        return

    if y==n:   # n에 도착하면
        if sofar < init_sum:   # 이번 단계의 계산값과, 이전의 계산값과 비교하여 작으면
            init_sum = sofar   # 교체하고, 아니면 건들지 않는다
        return

    for k in range(1,8):
        if info[y][k] != 0:    # 1에서 출발가능한 곳이 있으면
            dfs(k, sofar + info[y][k])

dfs(1,0)
print(init_sum)

