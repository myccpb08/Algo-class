import sys
sys.stdin = open('hw4.txt')

def bfs(here):
    global front, rear, visited
    rear+=1
    que[rear] = here
    visited[here]=1

    while front != rear:
        front += 1
        here = que[front]

        if here == end:
            return

        for next in range(1,v+1):
            if mymap[here][next]==1 and not visited[next]:
                visited[next] = 1
                distance[next] = distance[here]+1
                rear += 1
                que[rear] = next


for test in range(int(input())):
    v,e = map(int,input().split())   # v=노드 수, e=간선 수

    # 필요한 요소들
    mymap = [[0]*(v+1) for i in range(v+1)]
    visited = [0]*(v+1)
    que = [0]*(v+1)
    distance = [0]*(v+1)
    front = rear = -1



    for i in range(e):
        start,end = map(int,input().split())
        mymap[start][end]=1
        mymap[end][start]=1  # 길 정보 입력


    start,end = map(int,input().split())



    bfs(start)  # 입력받은 start 지점에서 탐색 시작

    print(f'#{test+1} {distance[end]}')