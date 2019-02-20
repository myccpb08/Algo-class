import sys
sys.stdin = open('04.txt', 'r')

for i in range(1, 11):
    n = input()
    grid = [[0]*102 for i in range(100)]  # 좌우 여백을 주고, 길이는 제공되는 대로 만든다, visit 와 grid
    for j in range(100):
        grid[j][1:101] = list(map(int, input().split()))  # 좌우 여백 제외하고, 입력받은 값으로 사다리 완성
    visit = [[0]*102 for i in range(100)]
    two = grid[99].index(2)  # 2의 위치. 역추적 해 나가야 한다
    dx = [-1, 1, 0]
    dy = [0, 0, -1]  # 좌 우 상
    y, x = 99, two

    while True:
        visit[y][x] = 1
        for j in range(3):
            nX, nY = x+dx[j], y+dy[j]
            if grid[nY][nX] and visit[nY][nX] != 1:
                x, y = nX, nY
                break
        if y == 0:
            print(f'#{i} {x-1}')
            break

