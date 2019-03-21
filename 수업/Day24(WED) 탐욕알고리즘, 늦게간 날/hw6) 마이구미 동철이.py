import sys
sys.stdin = open('동철.txt','r')

def getsome(depth,compare):
    global start
    if compare < start:
        return
    if depth == worker:
        if compare > start:
            start=compare
        return
    for i in range(worker):
        if not visited[i]:
            visited[i] = True
            getsome(depth + 1, compare*data[i][depth]/100)
            visited[i] = False

for tc in range(int(input())):
    worker = int(input())
    data=[]
    for info in range(worker):
        data.append(list(map(int,input().split())))

    start=1
    for i in range(worker):
         start *= data[worker-1-i][i]/100

    visited = [0]*worker
    result = [0]*worker

    getsome(0,1)
    print("#%d %0.6f" %(tc+1,start*100))