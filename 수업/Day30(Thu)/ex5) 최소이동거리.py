import sys, heapq
sys.stdin = open('최소이동거리.txt', 'r')

# 다익스트라 알고리즘
def solve(adjacent, K):  # k는 출발지
    prev = [-1] * (len(adjacent) + 1)    # predecessor
    dist = [10] * (len(adjacent) + 1)   # source로부터의 최소 거리 배열
    dist[K] = 0

    priority_queue = []   # 최소힙
    heapq.heappush(priority_queue, [0, K])   # 세트로 들어오면, 뒤를 기준으로 최소힙 만듦   (현재거리, 현재위치)

    while priority_queue:
        # 거리가 제일 작은 노드 선택
        current_dist, here = heapq.heappop(priority_queue)   # 최소힙으로 구성된 리스트에서 최솟값을 pop 시켜줌

        # 인접 노드 iteration
        for there, length in adjacent[here].items():   # in 현재위치에서 {갈 수 있는 곳: 거리}
            next_dist = dist[here] + length

            if next_dist < dist[there]:
                dist[there] = next_dist
                prev[there] = here
                heapq.heappush(priority_queue, [next_dist, there])

    return dist, prev


for tc in range(int(input())):
    V, E = map(int, input().split())
    adjacent = [{} for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())

        # 만약 동일한 경로의 간선이 주어질 경우 적은 비용의 간선 선택
        if v in adjacent[u]:
            adjacent[u][v] = min(adjacent[u][v], w)
        else:
            adjacent[u][v] = w

    dist, prev = solve(adjacent, 0)  # 출발지가 0

    print('#{} {}'.format(tc+1, dist[V]))