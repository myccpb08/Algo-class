

for i in range(int(input())):  # 테스트 케이스 수
    size = int(input())   # 섬 사이즈
    grid = [list(map(int,input().split())) for j in range(size)]

    # 섬 가장 높은 곳 찾기
    high = []
    for y in range(size):
        high += [max(grid[y])]

    highest = max(high)


    # 연결된 섬찾기
    def island(y,x):
        visited[y][x]=count   # visited 를 섬번호로 찍고

        dx=[-1,1,0,0]
        dy=[0,0,-1,1]

        for dir in range(4):
            ny=y+dy[dir]
            nx=x+dx[dir]
            if 0<=ny<size and 0<=nx<size and visited[ny][nx]==0 and grid[ny][nx]!=0:
                island(ny,nx)

    # 섬탐색, 섬 개수 찾기
    count = 0
    visited = [[0]*size for k in range(size)]
    for y in range(size):
        for x in range(size):
            if grid[y][x]!=0 and visited[y][x]==0:  #육지이고, 방문한 적 없으면, 탐색시작
                count += 1
                island(y,x)

    print('#{} {} {}'.format(i+1, count, highest))