import sys
sys.stdin = open('농작물.txt', 'r')

for i in range(int(input())):
    s=int(input())
    g=[list(map(int,list(input()))) for j in range(s)]
    m=0
    for y in range(s):
        dx=min(y,s-y-1)
        m+=sum(g[y][s//2-dx:s//2+dx+1])
    print('#{} {}'.format(i+1,m))