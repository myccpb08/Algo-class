import sys
sys.stdin = open('점심시간.txt', 'r')

for t in range(int(input())):
    print('#{}'.format(t+1))
    N=int(input())  # 판 사이즈
    D=[list(map(int,input().split())) for i in range(N)]  # 위치판

    P = []  # 사람
    S = []  # 계단

    for y in range(N):
        for x in range(N):
            if D[y][x]==1:
                P+=[(y,x)]     # [(0, 1), (0, 2), (1, 2), (2, 1), (2, 3), (4, 0)]
            if D[y][x]>1:
                S+=[(y,x,D[y][x])]    # [(1, 4, 3), (4, 2, 5)]

    road = []     # 한 사람이, 각 계단까지의 거리 + 출발시간 + 각 계단을 통과   까지 걸리는 시간 담음
                        # [(8, 11), (7, 10), (6, 9), (8, 9), (6, 9), (11, 8)]

    for person in P:
            road += [(abs(person[0]-S[0][0])+abs(person[1]-S[0][1])+1+S[0][2],  abs(person[0]-S[1][0])+abs(person[1]-S[1][1])+1+S[1][2])]

    first = 0  # 첫번째 계단이 가까운 사람 수
    second = 0
    idx = 0
    result = []

    for i in road:
        if i[0] < i[1] :   # 첫번째 계단으로 가는 게 더 가까운 사람
            first += 1
            result += [(i[0],1,idx)]
            idx += 1
        else:
            second += 1
            result += [(i[1], 2, idx)]
            idx += 1

    result.sort()   #[(6, 1, 2), (6, 1, 4), (7, 1, 1), (8, 1, 0), (8, 1, 3), (8, 2, 5)]

    for i in result:
        if first>3 :   # 첫번째 계단 사람이 3보다 더 많으면
            i[0] = 
