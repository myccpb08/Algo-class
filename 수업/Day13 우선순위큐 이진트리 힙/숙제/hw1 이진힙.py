# 1. 힙에 넣는다
# 2. 우선순위 조건(최소, 최대)에 맞춰 자리 이동시킨다
# 3. 이 문제는 최소힙이니까, root 가 자식보다 작아야 한다

for i in range(int(input())):
    node = int(input())
    data = [0] + list(map(int,input().split()))
    tree = [0]*(node+1)
    tree[1]=data[1]

    for element_index in range(2, node+1):  # 트리요소로 받아와야 할 요소들 호출
        tree[element_index]=data[element_index]  # 트리에, 요소를 일단 넣는다. 💘 일단 넣고 시작해야한다 💦 자꾸 틀렸던 이유

        # 비교해서 자리바꾸기 시작
        while element_index!=1:  # 현재 주인공이 루트면, 더이상 비교하지 않는다
            if tree[element_index] > tree[element_index //2]:  # 힙 조건에 맞으면
                break

            elif tree[element_index] < tree[element_index //2]: ## 새로들어온 자식이 부모보다 작으면
                tree[element_index], tree[element_index//2] = tree[element_index//2], tree[element_index]  # 교환한다
                element_index = element_index // 2

    answer = 0
    start = node//2
    while start!=0:
        answer += tree[start]
        start = start//2

    print('#{} {}'.format(i+1,answer))