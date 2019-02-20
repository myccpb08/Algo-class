import sys
sys.stdin = open('04.txt', 'r')

def Pass(y,x):   # 이동할 영역이, 사다리판 내부에 있는지 확인하는 함수
    if 0<=x<100 and 0<=y<100:
        return True
    else:
        return False

for i in range(1,11): # 테스트 케이스
    n = int(input())
    grid=[list(map(int,input().split())) for j in range(100)]  # 사다리판 만들기

    end = grid[99].index(2)  # 도착지점 2의 인덱스 찾기
    visited = [[0]*100 for _ in range(100)] # 방문할 곳 저장하는 위치
    k=98
    while True:
            if k == 0:   # 제일 윗칸까지 올라오면
                print(f'#{i} {end}') # 프린트를 하고
                break  # while 을 끝낸다

            if Pass(k,end-1) and grid[k][end-1]==1 and not visited[k][end-1] : # 가야할 곳이, 왼쪽인 grid[k][end-1] 이니까 이곳이 인덱스범위를 넘어가지 않는지 먼저 확인하는 pass 를 앞에 써준다
                                                                                                                        # 인덱스 범위 안에 있고, 왼쪽이 1이면, 왼쪽으로 이동한다
                visited[k][end] = 1 # 방문한 곳은 visited 를 1로 바꿔 저장
                end -= 1

            elif Pass(k,end+1) and grid[k][end+1]==1 and not visited[k][end+1]: # 가야할 곳(오른쪽) 의 인덱스 범위를 테스트하고, 이동 가능하면 이동
                visited[k][end] = 1 # 방문한 곳은 visited 를 1로 바꿔 저장
                end += 1

            elif Pass(k-1,end) and not visited[k-1][end]: # 위로가는 방향도 마찬가지로
                visited[k][end] = 1
                k -= 1










    #print(f'{i} {answer}')