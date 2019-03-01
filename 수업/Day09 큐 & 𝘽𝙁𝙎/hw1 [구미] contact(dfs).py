import sys
sys.stdin = open('hw2.contact.txt','r')

for i in range(1,11):
    path,start=map(int,input().split())
    info=list(map(int,input().split()))
    vertex = max(info)
    mymap=[[0]*(vertex+1) for j in range(vertex+1)]
    stack=[start]
    visited=[0 for _ in range(vertex+1)]
    visited[start]=1# 스택에 일단 start 넣어놓고
    done={ i:[] for i in range(1,vertex+1)}

    for j in range(0,path,2):
        mymap[info[j]][info[j+1]]=1  # 지도에 길 표시

    while len(stack)!=0:
        start = stack.pop()  # start 할 곳 큐에서 꺼냄
        for next in range(vertex+1):
            if mymap[start][next]==1 and (not visited[next] or (visited[next]!=0 and visited[start]+1 < visited[next])):
                temp=visited[start] + 1
                done[temp]+=[next]
                stack+=[next]  # 큐에 다음 출발지를 저장한다
                visited[next]=temp # 다음 출발지는 방문했다고 처리한다
    M=max(visited)
    result=0
    for k in range(1,vertex+1):
        if visited[k] == M and k>result:
            result=k
    print(f'#{i} {result}')