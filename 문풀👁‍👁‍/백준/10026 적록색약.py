import sys
sys.setrecursionlimit(100000)

def color_normal(y,x,visit):
    visit[y][x]=1

    for i in range(4):
        new_y, new_x = y+dy[i], x+dx[i]
        if 0<=new_y <size and 0<=new_x <size and visit[new_y][new_x]==0 and grid[new_y][new_x]==grid[y][x]:
            color_normal(new_y,new_x, visit)


size = int(input())
grid = [list(input()) for i in range(size)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited = [[0]*size for i in range(size)]

count = 0
for y in range(size):
    for x in range(size):
        if visited[y][x]==0:
            count += 1
            color_normal(y,x,visited)

print(count, end=' ')

# 색맹
visited2 = [[0]*size for i in range(size)]
for y in range(size):
    for x in range(size):
        if grid[y][x]=='R':
            grid[y][x]='G'

count = 0
for y in range(size):
    for x in range(size):
        if visited2[y][x]==0:
            count += 1
            color_normal(y,x,visited2)

print(count)