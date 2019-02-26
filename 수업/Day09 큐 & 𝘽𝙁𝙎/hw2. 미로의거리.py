def maze(info, start, end):
    global distance
    qu = []
    done = []
    qu.append(start)
    done.append(start)
    while qu:
        start = qu.pop(0)
        for i in range(4):
            new_y = start[0] + dy[i]   # 상하좌우
            new_x = start[1] + dx[i]
            new_start = (new_y, new_x)
            if new_start == end:
                return distance[start[0]][start[1]]+1
            else:
                if 0 <= new_y < size and 0 <= new_x < size and maze_grid[new_y][new_x]!=1 and (new_y, new_x) not in done:
                    qu.append(new_start)
                    done.append(new_start)
                    distance[new_y][new_x]=distance[start[0]][start[1]]+1
    return  0

dy = [-1,1,0,0]
dx = [0,0,-1,1]

for i in range(int(input())): # 테스트 케이스 수
    size = int(input())  # 미로판 사이즈
    maze_grid = [ list(map(int,input())) for j in range(size)]  # 미로판 정보 입력
    distance = [[-1]*(size) for j in range(size)]

    for y in range(size):
        for x in range(size):
            if maze_grid[y][x]==2:
                start = (y,x)   # 출발 정보 저장
            if maze_grid[y][x]==3:
                end = (y,x)  # 도착 정보 저장

    print(f'#{i+1} {maze(maze_grid, start, end)}')





