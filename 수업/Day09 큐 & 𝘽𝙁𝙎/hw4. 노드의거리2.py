import sys
sys.stdin = open('hw4.txt')

for test in range(int(input())):
    v,e = map(int,input().split())   # v=노드 수, e=간선 수

    # 필요한 요소들
    mymap = [[0]*(v+1) for i in range(v+1)]
    visited = [0]*(v+1)
    distance = [0]*(v+1)
    front = rear = -1


    # 길 정보 입력
    for i in range(e):
        start,end = map(int,input().split())
        mymap[start][end]=1
        mymap[end][start]=1

    start,end = map(int,input().split())

    que=[start]
    visited[start]=1

    while True:
        if end in que:
            break
        else:
            for next in range(1,v+1):
                if visited[next]==0 and mymap[start][next]==1 and next not in que:
                    visited[next]=visited[start]+1
                    que += [next]

            start = que.pop(0)

    print(f'#{test+1} {visited[end]-1}')