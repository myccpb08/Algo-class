import sys
sys.stdin = open("hw4.txt", "r")

for t in range(10):

    z=input()

    grid = [list(map(int, input().split())) for i in range(100)]

    row_group = []
    column_group = []
    cross_left_sum = cross_right_sum = 0

    for y in range(100):

        row_sum = column_sum = 0

        cross_left_sum += grid[y][y]
        cross_right_sum += grid[y-1][y-1]

        for x in range(100):

            row_sum += grid[y][x]
            column_sum += grid[x][y]

        row_group += [row_sum]
        column_group += [column_sum]

    total = row_group + column_group + [cross_left_sum]+[cross_right_sum]

    print(f'#{t+1} {max(total)}')