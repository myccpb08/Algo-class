for i in range(int(input())):
    n,m=map(int,input().split())
    f=[list(map(int,input().split())) for i in range(n)]
    d=[]
    for k in range(n-m+1):
        for j in range(n-m+1):
            c=0
            for l in range(m):
                c+=sum(f[j+l][k:k+m])
            d+=[c]
    print('#{} {}'.format(i+1,max(d)))