import sys
sys.stdin = open('보급로.txt', 'r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]   # 우 하 좌 상

def supply(y,x,sofar):

    if y==size-1 and x==size-1:
        return

    for i in range(4):
        new_y = y+dy[i]
        new_x = x+dx[i]
        if 0<=new_y<size and 0<=new_x<size:  #  인덱스 범위 내부의 곳이면
            temp = sofar + grid[new_y][new_x]  # 임시 비교용으로 값 만듦
            if 0<=visited[size-1][size-1]<=temp :  # 이미 도착지점에 기록된 값이 다음 위치값을 더한 값보다 작으면/-1이면 아직 미도착 상태
                continue   # 할 필요 없음

            if visited[new_y][new_x]==-1:   # 아예 아직 안 간 곳이면
                visited[new_y][new_x]=temp  # visited 값을 바꾸고
                supply(new_y, new_x, temp)  # 새로운 함수 실행
            else:  # 갔던 곳이지만
                if visited[new_y][new_x]>temp:   # 그 자리에 저장된 값이, 임시값보다 크면 다시 그길로 더 작은 값으로도 갈 수 있는 거니까
                    visited[new_y][new_x]=temp   # 작은 값으로 교환
                    supply(new_y,new_x,temp)

for tc in range(int(input())):
    size = int(input())
    grid = [list(map(int,input())) for i in range(size)]
    visited = [[-1]*size for i in range(size)]  # visited 를 값 기록으로 바꾸는 게 낫나?
    visited[0][0]=0
    print('#{}'.format(tc+1), end=' ')
    supply(0,0,0)
    print(visited[size-1][size-1])

    # 1 2
    # 2 2
    # 3 8
    # 4 57
    # 5 151
    # 6 257
    # 7 18
    # 8 160
    # 9 414
    # 10 395




