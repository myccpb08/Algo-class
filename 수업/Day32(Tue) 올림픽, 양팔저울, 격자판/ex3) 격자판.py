import sys
sys.stdin = open('격자판.txt','r')

def num(y,x,what,cnt):
    global done
    if cnt==6:
        done+=[what]
        return
    else:
        for dir in range(4):
            ny,nx=y+dy[dir],x+dx[dir]
            if 0<=ny<4 and 0<=nx<4:
                num(ny,nx,what*10+grid[ny][nx],cnt+1)

dx=[1,0,-1,0]
dy=[0,1,0,-1]
for t in range(int(input())):
    grid=[list(map(int,input().split())) for i in range(4)]
    done=[]
    for y in range(4):
        for x in range(4):
            num(y,x,grid[y][x],0)
    print('#{} {}'.format(t+1,len(set(done))))