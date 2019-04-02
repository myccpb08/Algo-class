import sys
sys.stdin=open('2105 디저트.txt','r')

dx = [1,1,-1,-1]
dy = [1,-1,-1,1]

def snack(y,x,dir):
    global result,cnt,ate
    # 방향 선택은 원래 방향이거나, 다음 방향 가거나 = 2가지
    for i in range(2):
        if dir+i==4: # 마지막 방향에 도달했으면
            return
        else:
            ny=y+dy[dir+i]
            nx=x+dx[dir+i]
            if ny==start_y and nx ==start_x:  # 출발지에 도착했으면
                cnt = ate.count(1)
                if result<cnt:  # 카운트 된 디저트 개수가 더 많으면
                    result=cnt
                return
            if 0<=ny<size and 0<=nx<size and ate[grid[ny][nx]]==0:
                ate[grid[ny][nx]]=1
                snack(ny,nx,dir+i)
                ate[grid[ny][nx]]=0

for t in range(int(input())):
    size=int(input())
    grid=[list(map(int,input().split())) for i in range(size)]
    result=-1
    for y in range(1,size-1):
        for x in range(size-2):
            cnt=1
            ate = [0]*(101)
            start_y, start_x = y, x
            ate[grid[y][x]] = 1
            snack(y,x,0)

    print('#{} {}'.format(t+1,result))