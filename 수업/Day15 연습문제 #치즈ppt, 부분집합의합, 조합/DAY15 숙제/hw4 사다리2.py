import sys
sys.stdin = open('hw2.txt','r')

dx=[-1,1,0]
dy=[0,0,1] # 왼,오,하

def ice(y,x):
    global distance
    visit[y][x]=1
    if y==99:
        return distance

    for m in range(3):
        ny,nx = y+dy[m], x+dx[m]
        if 0<=ny<=99 and 0<=nx<=99 and ladder[ny][nx]=='1' and visit[ny][nx]==0:
            distance+=1
            return ice(ny,nx)


for i in range(10):
    input()
    ladder=[input().split() for j in range(100)]
    mymin = 1000
    myindex = 0
    for j in range(100):
        if ladder[0][j]=='1':
            distance=0
            visit=[[0]*100 for k in range(100)]
            a=ice(0,j)
            if a<=mymin:
                mymin=a
                myindex=j

    print('#{} {}'.format(i+1,myindex))
