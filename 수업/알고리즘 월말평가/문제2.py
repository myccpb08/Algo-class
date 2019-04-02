import sys
sys.stdin = open('문제2.txt', 'r')

start = -987654321
for tc in range(int(input())):
    vertical, horizon = map(int,input().split())
    grid = [list(map(int,input().split())) for i in range(vertical)]

    for v in range(1,vertical):  # 전체 라인 중, v 라인을 선택했을 때
        for h1 in range(1,horizon-1): # 전체 라인 중, h1 라인을 선택했을 때
            for h2 in range(h1+1, horizon): # h1 라인 이후, h2 라인을 선택했을 때

                one, two, three, four, five, six = 0,0,0,0,0,0

                for y in range(v):
                    one += sum(grid[y][:h1])
                    two += sum(grid[y][h1:h2])
                    three += sum(grid[y][h2:])

                for y in range(v,vertical):
                    four += sum(grid[y][:h1])
                    five += sum(grid[y][h1:h2])
                    six += sum(grid[y][h2:])

                data = [one, two, three, four, five, six]

                choice = [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 2, 3),
                          (0, 2, 4), (0, 2, 5), (0, 3, 4), (0, 3, 5), (0, 4, 5),
                          (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5),
                          (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]

                for nth in range(15):
                    position = choice[nth]
                    region1 = position[0]
                    region2 = position[1]
                    region3 = position[2]
                    temp = abs(data[region1]-data[region2])+abs(data[region2]-data[region3])+abs(data[region3]-data[region1])
                    if temp > start:
                        start = temp

    print('#{} {}'.format(tc+1, start))