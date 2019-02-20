import sys
sys.stdin = open('04.txt', 'r')

def DFS(x,y):
    visited[y][x]=1
    for j in range(3):
            nX, nY = x + dx[j], y + dy[j]
            if grid[nY][nX] and not visited[nY][nX]:
                x, y = nX, nY
                break
    if y==0:
        return print(f'#{i} {x-1}')
    else:
        DFS(x,y)


for i in range(1,11):
    n=input()
    grid = [[0]*102 for i in range(100)]
    visited = [[0]*102 for i in range(100)]
    for j in range(100):
        grid[j][1:101] = list(map(int, input().split()))
    dx,dy=[-1,1,0],[0,0,-1]
    t=grid[99].index(2)
    y,x=99,t

    DFS(x,y)





