for i in range(int(input())):
    n,s=map(int,input().split())
    a=set([i for i in range(1,n+1)])
    for j in list(map(int,input().split())):
        a-={j}
    print('#{}'.format(i+1),end=' ')
    [print(k,end=' ') for k in a]
    print()