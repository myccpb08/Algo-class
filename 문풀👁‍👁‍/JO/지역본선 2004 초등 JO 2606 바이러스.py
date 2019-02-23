computer = int(input())
net = int(input())

my_map = [[0]*(computer+1) for i in range(computer+1)]
visit = [0] * (computer+1)

def DFS(here):
    visit[here] = 1
    for next in range(computer+1):
        if my_map[here][next] == 1 and visit[next] ==0:
            DFS(next)

for i in range(net):  # net 수만큼 정보를 받아들여서, 갈 수 있는지 저장한다
    start, end = map(int, input().split())
    
    my_map[start][end] = 1
    my_map[end][start] = 1


DFS(1)

print(visit.count(1)-1)