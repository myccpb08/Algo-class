def work(info):
    truck = 0
    start = info.pop(0)  # 제일 빨리 작업하는 애를 시작으로 선정
    truck += 1

    while len(info)!=0:  # 갈 지점이 남아있는 동안
        flag=0
        end_time = start[1]
        for k in range(len(info)):
            if info[k][0]>=end_time:      # 다음 시작점이 앞에서 끝난 점보다 같거나 뒤인 게 있으면,
                start = info.pop(k)  # 다음 트럭
                truck += 1
                info = info[k:]
                break
            if k==len(info)-1:  # 다음 출발지를 못 찾고 인덱스가 끝나버렸으면
                flag=1
                break
        if flag==1 or info==[]:
            return truck


for i in range(int(input())):
    n=int(input())
    info = []
    for j in range(n):
        part=tuple(map(int,input().split()))
        info.append(part)

    info.sort(key=lambda x : x[1])
    a=work(info)
    print('#{} {}'.format(i+1,a))