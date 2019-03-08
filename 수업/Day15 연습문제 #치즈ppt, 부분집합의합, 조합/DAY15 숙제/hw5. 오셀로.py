import sys
sys.stdin = open('hw2.txt','r')

# 보드는 4,6,8
# 흑이 선공

# 상 하 좌 우 좌상 우상 좌하 우하 : 8방향
dx=[0,0,-1,1,-1,1,-1,1]
dy=[-1,1,0,0,-1,-1,1,1]

def othello(y,x,stone):
    my[y-1][x-1]=stone

    for k in range(8):
        visit = []
        nx = x - 1
        ny = y - 1
        while True:
            nx += dx[k]
            ny += dy[k]
            if not 0<=nx<n or not 0<=ny<n:  # 인덱스 범위 안에서
                break

            if my[ny][nx]==0:
                break

            elif my[ny][nx]==stone:  # 나랑 같은 돌이면
                for point in visit:
                    my[point[0]][point[1]]=stone
                break

            else: # 상대방 돌이면
                visit += [(ny,nx)]


for i in range(int(input())):
    n,m=map(int,input().split())   # n:사이즈, m:시도 수
    a=n//2
    my=[[0]*n for j in range(n)]
    my[a-1][a-1]=my[a][a]=2  # 백돌
    my[a-1][a]=my[a][a-1]=1  # 흑돌

    # 돌 놓아라
    for j in range(m):
        y,x,stone=map(int,input().split())
        othello(y,x,stone)

    # 돌 수 세기
    B,W=0,0
    for y in range(n):
        for x in range(n):
            if my[y][x]==1:B+=1  # 흑돌 수 카운트
            elif my[y][x]==2:W+=1 # 백돌 수 카운트

    print('#{} {} {}'.format(i+1,B,W))
