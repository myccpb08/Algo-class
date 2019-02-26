a=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

max_node = max(a)

visited = [0]*(max_node+1)

matrix = [[0]*(max_node+1) for i in range(max_node+1) ]

# 길 표시
for i in range(len(a)//2):
    head = a[2*i]
    tail = a[2*i+1]
    matrix[head][tail] = 1
    matrix[tail][head] = 1

que = [1]
road = []
y=1
visited[1]=1

while len(road)!=max_node:
    for x in range(1,max_node+1):
        if visited[x]==0 and matrix[y][x]==1 and x not in que:  # 방문하지 않았고, 길이 있고, que 에 없으면
            visited[x]=visited[y]+1  # 방문했다고 찍고
            que += [x]  # 큐에 넣는다


    next_start = que.pop(0)   # 큐에 맨 처음 저장 된 걸 다음 출발지로 하고,
    y = next_start
    road += [next_start]

print(road)
[ print(f'{i} 의 길이는 {visited[i]-1} 입니다') for i in range(1,max_node+1)]

