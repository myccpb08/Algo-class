import sys
sys.stdin = open('hw3.txt','r')

# 오목판 정보 받기
a=[[0]*29 for i in range(5)]
for i in range(19):
    a+= [[0]*5+list(map(int,input().split())) + [0]*5]

a+=[[0]*29 for i in range(5)]

# 방향키 ( 무조건 왼쪽 좌표가 필요)
dy=[0,1,-1,1]
dx=[1,0,1,1]   # 오-하-우상-오하

def badook():
    for x in range(5,25):
        for y in range(5,25):
            if a[y][x] in [1,2]:  # 흰색이나 바둑돌이면
                for i in range(4):   # 4방향에 대하여
                    if a[y][x]==a[y+4*dy[i]][x+4*dx[i]]==a[y+3*dy[i]][x+3*dx[i]]==a[y+2*dy[i]][x+2*dx[i]]==a[y+1*dy[i]][x+1*dx[i]]!=a[y+5*dy[i]][x+5*dx[i]]:
                        if a[y][x]!=a[y-1*dy[i]][x-1*dx[i]]:
                            flag = 1
                            return (flag,y,x)
    flag = 0
    return (flag, 0, 0)


if badook()[0]==1:
    print(a[badook()[1]] [badook()[2]])
    print(badook()[1]-4,badook()[2]-4)
else:
    print(0)