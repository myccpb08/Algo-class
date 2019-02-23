import sys
sys.stdin = open('input.txt', 'r')

def DFS(here):
    visit[here] = 1
    for next in range(node + 1):
        if my_map[here][next] == 1 and not visit[next]:  # 이동가능하고 방문하지 않았으면
            DFS(next)

for i in range(int(input())):
    node, path = map(int, input().split())  # node 개수, path 개수

    my_map = [[0]*(node+1) for i in range(node+1)]   # 길 말해주는 map
    visit = [0]*(node+1)   # 방문해준 곳

    for j in range(path): # 길 수만큼 길정보를 업데이트 해 줌
        start, end = map(int,input().split())
        my_map[start][end] = 1

    start, want_end = map(int, input().split())

    DFS(start)

    if visit[want_end]==1:
        print(f'#{i + 1} 1')
    else:
        print(f'#{i + 1} 0')





