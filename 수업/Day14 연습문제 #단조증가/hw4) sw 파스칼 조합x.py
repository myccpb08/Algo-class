for i in range(int(input())):
    n=int(input())
    print('#{}\n1'.format(i+1))
    if n!=1:
        a=[[1,1]]
        for j in range(n-2):
            b=[1]
            for k in range(len(a[j])-1):
                b+=[a[j][k]+a[j][k+1]]
            b+=[1]
            a+=[b]
        for i in a:
            print(*i)