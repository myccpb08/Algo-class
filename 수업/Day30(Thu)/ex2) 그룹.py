import sys
sys.stdin = open('ex2.txt', 'r')

for tc in range(int(input())):
    student, friends = map(int,input().split())
    mymap = [ [0]*(student+1) for i in range(student+1)]
    data = list(map(int,input().split()))
    for i in range(0, len(data), 2):
        mymap[data[i]][data[i+1]]=1
        mymap[data[i+1]][data[i]]=1

    group = [-1]+[0]*(student)
    cnt = 0
    def find(y):
        global cnt
        if y==student+1:
            return

        for next in range(1, student+1):
            if mymap[y][next]==1 and group[next]==0:
                if group[y]==0:
                    cnt+=1
                    group[y]=cnt
                group[next]=cnt
        find(y+1)
    find(1)
    print(group)
    plus = group.count(0)
    print('#{} {}'.format(tc + 1, cnt+plus))