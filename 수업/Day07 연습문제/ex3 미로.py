import sys
sys.stdin = open('ex3 미로.txt', 'r')

def DFS(y,x):
    global result
    if grid[y][x] == 3:  # 미로의 도착지를 찾았으면
        result = 1      # 플래그를 1로 바꿈
    grid[y][x] = 1  # 자기꺼에서 갔던 곳 1로 바꿈
    for k in range(4):  # 다음 위치를 찾자
        nY = y + dy[k]
        nX = x + dx[k]
        if 0<=nY<n and 0<=nX<n and grid[nY][nX]!=1:   # 다음 위치가 길이고, 방문하지 않은 곳이면
            # x = nX
            # y = nY  쓰면, 기존에 주소를 건들기 때문에 오류난다

            DFS(nY, nX)


dx = [-1,1,0,0]
dy = [0,0,-1,1]


for i in range(int(input())):
    result = 0  # 플래그 역할
    n=int(input())
    grid = [list(map(int,input())) for j in range(n)]
    for j in range(n):
        if 2 in grid[j]:
            start_x = grid[j].index(2)
            start_y = j
    DFS(start_y, start_x)
    print(f'#{i+1} {result}')
