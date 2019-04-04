def babo(plus,minus,mul,div,sofar,choice):
    global mymin, mymax
    if plus==p and minus==m and mul == x and div==r:
        if sofar < mymin:
            mymin = sofar
        if sofar > mymax:
            mymax = sofar
        return
    else:
        if plus<p:
            babo(plus+1,minus,mul,div,sofar+num[choice+1],choice+1)
        if minus<m:
            babo(plus , minus+1, mul, div, sofar-num[choice+1], choice+1)
        if mul< x:
            babo(plus, minus, mul+1, div, sofar*num[choice+1], choice+1)
        if div<r:
            babo(plus, minus, mul, div+1, int(sofar/num[choice+1]), choice+1)

for t in range(int(input())):
    n=int(input())  # 3이상 12이하
    p,m,x,r=map(int,input().split())
    num=list(map(int,input().split()))
    mymin = 100000000
    mymax = -100000000
    babo(0,0,0,0,num[0],0)
    print('#{} {}'.format(t+1,mymax-mymin))