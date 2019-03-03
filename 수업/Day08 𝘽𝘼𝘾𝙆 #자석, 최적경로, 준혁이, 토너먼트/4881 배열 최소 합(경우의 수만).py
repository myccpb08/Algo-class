import sys
sys.stdin = open('4881.txt', 'r')

def GetSome(y):
    global visited
    global ans

    if y>n-1 :
        ans += 1
        return

    else:
        for x in range(0,n):
            if visited[x] != 1:   # x 열이 선택되지 않았으면
                visited[x] = 1   # x열을 선택하고 1로 바꿈
                GetSome(y+1)   # 다음 행에 시행
                visited[x] = 0


for i in range(int(input())):  # 테스트 케이스
    n=int(input())
    visited = [0]*n
    ans = 0
    grid = [ list(map(int,input().split())) for j in range(n)]

    GetSome(0)
    print(ans)