import sys
sys.stdin=open('올림픽.txt','r')

for t in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    vote=[0]*n
    for i in range(m):
        for j in range(n):
            if a[j]<=b[i]:
                vote[j]+=1
                break
    print('#{} {}'.format(t+1,vote.index(max(vote))+1))
