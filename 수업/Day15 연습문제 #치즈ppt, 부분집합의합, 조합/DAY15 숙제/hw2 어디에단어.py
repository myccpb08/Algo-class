import sys
sys.stdin = open('hw2.txt','r')

from copy import deepcopy
def tr(l,a):
    for y in range(a):
        for x in range(a):
            if y>x:
                l[y][x],l[x][y]=l[x][y],l[y][x]
    return l
for i in range(int(input())):
    a,b=map(int,input().split())
    m=[input().split() for j in range(a)]
    n,z=deepcopy(m),0
    c=tr(n,a)
    for k in [m,c]:
        for j in k:
            x=(''.join(j)).split('0')
            if '1'*b in x:
                z+=x.count('1'*b)
    print('#{} {}'.format(i+1,z))