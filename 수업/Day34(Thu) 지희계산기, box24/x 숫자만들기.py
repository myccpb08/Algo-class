import sys
sys.stdin = open('공통조상.txt','r')

def babo(plus,minus,mul,div,sofar):
    global mymin, mymax
    if [plus,minus,mul,div] == [p,m,x,r]: # 연산자 다 썼으면
        if sofar < mymin:
            mymin = sofar
        if sofar > mymax:
            mymax = sofar
        return
    else:
        if plus<p:
            babo(plus+1,minus,mul,div,)

for t in range(int(input())):
    print('#{}'.format(t+1))
    n=int(input())  # 3이상 12이하
    #op=list(map(int,input().split()))   # + - * /
    p,m,x,r=map(int,input().split())
    num=list(map(int,input().split()))

    mymin = 100000000
    mymax = -100000000
    babo(0,0,0,0,0)  # plus, minus, mul, div, sofar
