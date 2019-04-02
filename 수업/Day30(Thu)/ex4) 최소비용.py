import sys
sys.stdin = open('최소비용.txt', 'r')

# 하우상좌
dy = [1,0,-1,0]
dx = [0,1,0,-1]

def fun(y,x,sofar):
    global temp

    if sofar > temp: # 최종 저장된 값보다, 커버리면 더 갈 필요없음
        return

    if y==size-1and x==size-1: # 목적지에 도착하면
        if sofar < temp: # 값비교하고 종료
            temp = sofar
        return

    for i in range(4):
        next_y, next_x = y+dy[i], x+dx[i]
        if -1<next_y<size and -1<next_x<size:  # 인덱스 범위에 있고, 방문한 적이 없다
            # 현재 위치와, 다음 위치의 높이가 같다
            if data[visited[next_y][next_x]==-1 or visited[next_y][next_x] > visited[y][x]+1








for tc in range(int(input())):
    size = int(input())
    grid = [list(map(int,input().split())) for i in range(size)]
    temp = 987654321
    visited = [[-1]*(size) for i in range(size)]
    fun(0,0,0)

