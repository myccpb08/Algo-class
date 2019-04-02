import sys
sys.stdin = open('문제3.txt', 'r')


def find(y,sofar):
    global temp
    if y == n:
        if sofar < temp:
            temp = sofar
        return
    if sofar > temp:
        return
    for x in range(n):
        if visited[x]==0:
            visited[x]=1
            find(y+1,sofar+distance[y][x])
            visited[x]=0

for tc in range(int(input())):
    n = int(input())
    snack = list(map(int,input().split()))
    robot = list(map(int,input().split()))

    distance = [[0]*n for i in range(n)]

    for i in range(n):  # 스낵좌표
        for j in range(n):
            distance[i][j] = abs(snack[2*i]-robot[2*j])+abs(snack[2*i+1]-robot[2*j+1])


    visited = [0]*n
    temp = 987654321

    find(0,0)

    print('#{} {}'.format(tc+1, temp))