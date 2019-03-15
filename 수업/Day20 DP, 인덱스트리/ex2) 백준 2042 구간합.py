import sys
sys.stdin = open('ex3.txt', 'r')

def update(a,b):
    where = base + a -1
    stree[where] = b
    where >>= 1
    while  where:
        stree[where] = stree[where*2] + stree[where*2 +1]
        where >>= 1

def RSQ2(ffrom, to):
    ffrom = ffrom + base -1
    to = to + base -1
    sum = 0
    while ffrom < to:
        if ffrom&1 :
            sum+=stree[ffrom]
            ffrom += 1
        if to&1==0:
            sum += stree[to]
            to -= 1
        ffrom >>=1
        to >>= 1
    if ffrom == to:
        sum += stree[ffrom]
    print(sum)


n, m, k = map(int,input().split())
base = 1
c = 1
while base <= n:
    base <<= 1
    c += 1

stree = [0]*(1<<c)
for i in range(base, base+n):
    stree[i]=int(input())
for parent in range(base-1, 0, -1):
    stree[parent] = stree[parent<<1] + stree[(parent<<1)+1]

for i in range(m+k):
    act, where, what = map(int,input().split())
    if act == 1:
        update(where, what)
    else:
        RSQ2(where,what)