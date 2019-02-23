import sys
sys.stdin = open('2667.txt', 'r')

# grid 생성
n=int(input())
grid = [[0]*(n+2)]
for i in range(n):
    grid += [[0]+list(map(int,input()))+[0]]
grid += [[0]*(n+2)]

# guest_book 생성
visit = [[0]*(n+2) for i in range(n+2)]

# 함수 정의
def DFS(y,x):
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]  # 좌 우 상 하
    visit[y][x]  = count   # 방문했다고 표시
    for next in range(4):
        nY = y + dy[next]
        nX = x + dx[next]
        if grid[nY][nX]==1 and visit[nY][nX]==0:
            DFS(nY,nX)




count = 0
for y in range(1,n+1):
    for x in range(1,n+1):
        if visit[y][x]==0 and grid[y][x]==1:
            count += 1
            DFS(y,x)

print(count)
z=[]
for i in range(1,count+1):
    c=0
    for y in range(n+2):
        for x in range(n+2):
           if visit[y][x]==i:
               c+=1
    z+=[c]
z.sort()
[print(i) for i in z]