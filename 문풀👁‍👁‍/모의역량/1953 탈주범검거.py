tunnel = [0,
                [(-1, 0), (1, 0), (0, 1), (0, -1)],
                [(-1, 0), (1, 0)],
                [(0, -1), (0, 1)],
                [(-1, 0), (0, 1)],
                [(1, 0), (0, 1)],
                [(1, 0), (0, -1)],
                [(-1, 0), (0, -1)]]

def go(new_y, new_x, start_y, start_x, dir):
    for i in tunnel[dir]:
        ny = new_y + i[0]
        nx = new_x + i[1]
        if (ny, nx) == (start_y, start_x):
            return True

def bfs(y, x):
    global cnt
    que = [(y, x)]
    visited = [[0] * h for i in range(v)]
    visited[y][x] = 1
    cnt = 1
    while que:
        start = que.pop(0)
        start_y = start[0]
        start_x = start[1]

        direction = grid[start_y][start_x]

        for i in tunnel[direction]:
            new_y = start_y + i[0]
            new_x = start_x + i[1]

            if 0 <= new_y < v and 0 <= new_x < h and grid[new_y][new_x] != 0 and visited[new_y][new_x] == 0 and go(
                    new_y, new_x, start_y, start_x, grid[new_y][new_x]):  # 인덱스 범위에 있고, 방문한 적이 없으면
                visited[new_y][new_x] = visited[start_y][start_x] + 1
                que += [(new_y, new_x)]
                if visited[new_y][new_x] > t:
                    return
                cnt += 1

for tc in range(int(input())):
    print('#{}'.format(tc + 1), end=' ')
    v, h, y, x, t = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(v)]
    bfs(y, x)
    print(cnt)