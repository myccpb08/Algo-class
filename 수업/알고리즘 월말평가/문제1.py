import sys
sys.stdin = open('문제1.txt', 'r')

for tc in range(int(input())):
    print('#{}'.format(tc+1), end=' ')
    size = int(input())
    data = list(map(int,input().split()))
    start = (data[0], data[1])
    end = (data[2], data[3])

    dx=[-2,-3,-2,-3,2,3,2,3]
    dy=[-3,-2, 3, 2,-3,-2,3,2]

    que = [start]
    done = []
    distance = {start:0}

    while que!=[]:
        start = que.pop(0)
        start_x = start[0]
        start_y = start[1]
        done += [(start)]

        if end[0]==start_x and end[1]==start_y:  # 도착했으면
            print(distance[end])
            break
        else:
            for i in range(8):  # 8방향에 대하여
                next_position = (start_x + dx[i], start_y + dy[i])
                if 0<=next_position[0]<size and 0<=next_position[1]<size and next_position not in que and next_position not in done:
                    que+=[(next_position)]
                    distance[next_position]=distance[start]+1
