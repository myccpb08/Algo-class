import sys
sys.stdin = open("input2.txt", 'r')

for k in range(1):
    v,e=map(int,input().split())  # v는 일 수, e 는 길 수 (input 에서 받아 오는 거)
    path=list(map(int,input().split()))  # input 에서 받아 오는 거

    road={}
    go=[]
    for j in range(v):  # 작업 수 만큼 반복, 길 저장하는 거
        road[j+1]=[]  # 일단 길 경우의수 빵으로 채워둠
    for j in range(e):  # path 에서 받아온 경우의 수
        road[path[2*j+1]]+=[path[2*j]]   # 길의 역정보 저장 : 일 완료가 중요하니까

    while True:
        if len(go) == v:
            break
        else:
            for i in range(1,v+1):
                if len(road[i])==0 and i not in go:  #go 에 없으면 넣어
                    go+=[i]

            for i in range(1,v+1):
                for j in road[i]:
                    if j in go:
                        del road[i][(road[i].index(j))]
    print(f'#{k+1}', end=' ')
    [print(i,end=' ') for i in go]

