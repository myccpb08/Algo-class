import sys
sys.stdin = open('ex2.txt','r')

def battery(move,min_sum,ffrom):
    global start
    if min_sum>=start:
        return

    if move==size:
        min_sum += grid[ffrom][0]
        if min_sum<start:
            start=min_sum

            return

    for to in range(1,size):  # 1,2
        #tmp = 0
        if ffrom!=to and visited[to]==0:  # 방문하지 않았으면
            visited[ffrom]=1
            battery(move+1, min_sum+grid[ffrom][to], to)
            visited[ffrom]=0

for tc in range(int(input())):
    size = int(input())
    grid =  [ list(map(int,input().split())) for i in range(size)]
    start = size*100
    visited = [0]*size
    # visited[0]=1
    battery(1,0,0)   # move, min_sum, ffrom
    print('#{} {}'.format(tc+1,start))
