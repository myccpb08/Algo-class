# 각 번호에 (Indegree = 들어오는 화살표) 를 기록하고, Indegree=0 인 곳이 최초 출발점이다
# 최초 출발점을 기록하고, 이 출발점의 child 들의 indegree 를 1씩 줄인다
# 그러다가 다시 indegree=0 인 숫자가 있으면, 다음 출발점으로 잡는다

for tc in range(1,11):
    V,E = map(int,input().split())
    print("#%d" %tc , end=' ')

    MyMap = [[0]*(V+1) for _ in range(V+1)]
    InDegree = [-1]+[0]*V   # 0은 범위에 없어서, 검색하지 않도록 -1 로 하고, 나머지는 0으로 설정

    Edges = list(map(int,input().split()))

    for i in range(E):
        parent, child = Edges[i*2: i*2+2]
        MyMap[parent][child] = 1
        InDegree[child] += 1

    while True: # bfs 와의 차이
        FoundSomething = False
        for what in range(1,V+1):
            if InDegree[what]==0:  # 출발가능한 곳을 발견하면
                FoundSomething = True
                print(what, end=' ')
                InDegree[what]=-1  # 다시 검색하지 않도록, 찍고 -1로 변경하고
                break  # 반복문 끊고

        for child in range(1,V+1):  # 이동가능한 자식 찾기
            if MyMap[what][child] and InDegree > 0:  # 길이 있는 자식
                InDegree[child] -= 1

        if not FoundSomething:  # 플래그로 빠져나오도록 하는 게, 쉽고 안전하다
                                # 출발지를 찾지 못하고 = 플래그가 false 인 상태
            break

        print()
