import sys
sys.stdin = open('4881.txt', 'r')

def GetSome(y,n,nowsum):
    global visited
    global init_sum

    if y>n-1 :
        if nowsum < init_sum:
            init_sum = nowsum
        return

    if nowsum > init_sum:
        return

    else:
        for x in range(n):
            if visited[x] != 1:   # x 열이 선택되지 않았으면
                nowsum += grid[y][x]
                visited[x] = 1   # x열을 선택하고 1로 바꿈
                GetSome(y+1,n,nowsum)   # 다음 행에 시행
                nowsum -= grid[y][x]
                visited[x] = 0



for i in range(int(input())):  # 테스트 케이스
    n=int(input())
    visited = [0]*n
    init_sum = 10*n
    grid = [ list(map(int,input().split())) for j in range(n)]

    GetSome(0,n,0)
    print(f'#{i+1} {init_sum}')