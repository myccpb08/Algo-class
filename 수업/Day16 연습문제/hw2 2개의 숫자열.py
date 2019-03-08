import sys
sys.stdin = open('hw2.txt','r')

for i in range(int(input())):
    c,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    e=a
    if c>d:  # 항상 a가 더 짧도록 설정
        a=b
        b=e
    f=[]
    for j in range(abs(c-d)+1):
        g=0
        for k in range(len(a)):
            g+=a[k]*b[j+k]
        f+=[g]
    print('#{} {}'.format(i+1,max(f)))