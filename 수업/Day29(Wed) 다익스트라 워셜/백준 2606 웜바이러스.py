import sys
sys.stdin = open('바이러스.txt', 'r')

def find(x):
    if x==mom[x]:
        return x
    else:
        return find(mom[x])

def union(x,y):
    mom[find(y)] = find(x)

n = int(input())
m = int(input())
mom = [0]*(n+1)
for i in range(n+1):
    mom[i]=i
for i in range(m):
    x,y = map(int,input().split())
    union(x,y)

cnt = -1
for j in range(1,len(mom)):
    if find(j) == find(1):
        cnt += 1

print(cnt)