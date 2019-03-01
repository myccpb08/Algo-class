import sys
sys.stdin = open('hw3.txt','r')

# 오목판 정보 받기
a=[]
for i in range(19):
    a+= [[0]*5+list(map(int,input().split()))+[0]*5]

print(a)

# 방향키
dy=[0,1,1,1]
dx=[1,0,-1,1]   # 오-하-왼하-오상-오하


# 일단 시작 돌 찾기

def badook():
    for x in range(5,25):
        for y in range(15):
            if a[y][x] in [1,2]:  # 흰색이나 바둑돌이면
                for i in range(8):   # 4방향에 대하여
                    if a[y][x]==a[y+4*dy[i]][x+4*dx[i]]==a[y+3*dy[i]][x+3*dx[i]]==a[y+2*dy[i]][x+2*dx[i]]==a[y+1*dy[i]][x+1*dx[i]]!=a[y+5*dy[i]][x+5*dx[i]]: # 4칸이동해도 같은 돌이면
                        if 0<y-1*dy[i] and 0<x-1*dy[i] :
                            if a[y][x]!=a[y-1*dy[i]][x-1*dy[i]]:
                                flag = 1
                                return (flag, y, x)
                        else:
                            flag = 1
                            return (flag,y,x)
if badook()[0]==1:
    print(a[badook()[1]][badook()[2]])
    print(badook()[1]+1,badook()[2]+1)
else:
    print(0)