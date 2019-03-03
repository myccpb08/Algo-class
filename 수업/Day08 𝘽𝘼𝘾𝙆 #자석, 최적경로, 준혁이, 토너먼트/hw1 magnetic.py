for i in range(10):

    n=int(input())
    grid=[list(map(int,input().split())) for j in range(n)]
    count=0

    for x in range(100):  # 한 열씩 검사
        sign='neutral'   # 새로운 열을 시작할 땐 중립으로 리셋
        for y in range(100):  # 한 행씩 내려가며 비교
            if grid[y][x]==1:   # 처음에 n 극이 걸리면 sign 을 레드로 줌
                sign='red'
            elif grid[y][x]==2 and sign=='red':  # 레드 sign 인 상태에서 아래 s 극이 오면 카운트
                sign='neutral'
                count+=1

    print(f'#{i+1} {count}')