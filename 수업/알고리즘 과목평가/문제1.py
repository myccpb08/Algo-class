for i in range(int(input())):
    gs, xs = map(int,input().split())
    grid = [list(map(int,input().split())) for j in range(gs)]

    left = []
    right = []

    # 왼쪽 계산
    for j in range(gs-xs+1):  # gs=4, xs=3 이면, j= 0 과 1  # 즉 y축
        for k in range(gs-xs+1): # 계산의 왼쪽 시작점은 grid[j][k]   # k도 0, 1 움직임 x
            start=0

            for dir in range(xs):
                start+=grid[j+dir][k+dir]
            left += [start]

    # 오른쪽 계산
    for j in range(gs-xs+1):  # j= 0 과 1
        for k in range(xs-1, gs):   # 오른쪽 계산의 시작점은 grid[j][k]   # k=2,3
            start=0
            for dir in range(xs):
                start += grid[j+dir][k-dir]
            right += [start]

    result = []

    for k in range((gs-xs+1)**2):
        answer = abs(right[k]-left[k])
        result += [answer]

    real_answer = min(result)
    print('#{} {}'.format(i+1,real_answer))