import sys
sys.stdin = open('신장.txt', 'r')

def find(x):
    if x==mom[x]:
        return x
    else:
        return find(mom[x])

def union(x,y):
    mom[find(y)] = find(x)

for tc in range(int(input())):
    node, path = map(int,input().split())
    mom = [ i for i in range(node+1)]
    data = []
    for i in range(path):
        start, end, weight = map(int,input().split())
        if start > end:
            start, end = end, start
        data.append((start,end,weight))

    data.sort(key=lambda x: x[2])  # weight 가 짧은 순으로 정렬

    tree= []
    tree_edges = 0
    mst_cost = 0
    while True:
        if tree_edges == node:  # 전부 연결했으므로
            break

        start, end, weight = data.pop(0)

        if find(start)!=find(end):  # start 와 end 의 조상이 서로 다르면
            union(start, end)   # start 와 end 를 연결
            tree_edges += 1   # 노드 하나 연결했음
            mst_cost += weight  # 가중치 추가했음
            tree.append((start,end))

    print('#{} {}'.format(tc+1, mst_cost))
    #print(tree)

