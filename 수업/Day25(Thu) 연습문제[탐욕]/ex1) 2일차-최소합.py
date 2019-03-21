import sys
sys.stdin = open('ex1.txt','r')

dir = [[1,0], [0,1]]
def mini(move, min_sum,y,x):
    global start
    if min_sum>=start:
        return

    if move==2*size-1:
        if min_sum<start:
            start = min_sum
            #data.append(min_sum)
        return

    if 0<=y<size and 0<=x<size and visited[y][x]==0:  # 범위에 있고 방문하지 않았으면
        visited[y][x]=1  #방문으로 표시
        for i in range(2):
            next_y=y+dir[i][0]
            next_x=x+dir[i][1]
            if 0<=next_y<size and 0<=next_x<size:
                mini(move+1, min_sum+grid[next_y][next_x], next_y, next_x)
                visited[next_y][next_x]=0


# 이동수는 2*size-1
for tc in range(int(input())):
    size = int(input())
    grid = [ list(map(int,input().split())) for i in range(size)]
    #data=[]
    visited = [[0]*size for i in range(size)]
    start = 250
    mini(1,grid[0][0],0,0)

    print('#{} {}'.format(tc+1, start))