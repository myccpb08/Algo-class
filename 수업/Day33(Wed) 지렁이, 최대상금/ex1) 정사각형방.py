import sys
sys.stdin = open('정사각형.txt', 'r')

# 하 우 상 좌
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move(y,x,value):
    global cnt
    for dir in range(4):
        ny,nx = y+dy[dir], x+dx[dir]
        if 0<=ny<n and 0<=nx<n and grid[ny][nx]-1==value:
            visited[grid[ny][nx]]=1
            cnt += 1
            move(ny,nx,grid[ny][nx])

for t in range(int(input())):
    n=int(input())
    grid=[list(map(int,input().split())) for i in range(n)]

    # 출발해야하는 방 번호와, 몇 개를 갈 수 있는지
    result = []
    count = 1
    start_point = 1000001
    visited = [0]*(n**2+1)
    for y in range(n):
        for x in range(n):
            if visited[grid[y][x]]==0 and grid[y][x]<=n**2-count:
                cnt = 1
                move(y,x,grid[y][x])
                if cnt >count:
                    count = cnt
                    start_point = grid[y][x]
                elif cnt ==count and grid[y][x] < start_point:
                    count = cnt
                    start_point = grid[y][x]

    print('#{} {} {}'.format(t+1,start_point,count))