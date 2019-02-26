


mymap = [[0]*8 for i in range(8)]
visited = [0]*8
que = [0]*8
parent = [-1]*8
Distance = [0]*8


def BFS(here):
    global front, rear
    rear += 1
    que[rear] = here
    visited[here] = True

    while front != rear:
        front += 1
        here = que[front]
        print(here)  # 경로 출력

        for next in range(8):
            if mymap[here][next] and not visited[next]:
                visited[next] = True
                Distance[next] = Distance[here]+1
                parent[next] = here
                rear += 1
                que[rear] = next




distance[1]=0
BFS(1)