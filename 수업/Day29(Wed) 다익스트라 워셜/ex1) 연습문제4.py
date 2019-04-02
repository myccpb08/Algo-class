# p339

import sys
sys.stdin = open('ex1.txt', 'r')

mymap = [[987654321]*6 for i in range(6)]
for i in range(10):
    start,end,distance = map(int,input().split())
    mymap[start][end]=distance

T = [0,1,2,3,4,5]
S = 0
Dist = mymap[0]  # 0 → 도착점 거리
#mom = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

while T!=[0]*6:   # T에 원소가 있는 동안 반복
    mini = Dist[0]
    for v in range(6):
        if T[v]!=0 and Dist[v]<mini:
            mini = Dist[v]
    v = Dist.index(mini)  # 처음에 1 선택
    T[v] = 0  # 1 제거
    for x in T:   # 2345 들어있음
        if x!=0:
            Dist[x] = min(Dist[x], Dist[v] + mymap[v][x])   # 그냥 0→2 vs 0→1→2 중 최소 선택
            #if Dist[x]==Dist[v]+mymap[v][x]:
                #mom[x] += [v]

Dist[0]=0
print(Dist)
#print(mom)