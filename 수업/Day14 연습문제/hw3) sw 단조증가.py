import sys
sys.stdin = open('단조증가.txt', 'r')

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for j in a:
        if j%10!=0:
            b+=[j]
    length=len(b)
    result=-1
    for j in range(length-1):
        for k in range(j+1,length):
            flag=1
            c2=b[j]*b[k]
            if c2 > result:
                c=str(c2)
                for t in range(len(c)-1):
                    if c[t]>c[t+1]:
                        flag=0
                        break
                if flag==1 and c2>result:
                    result = c2
    print('#{} {}'.format(i+1,result))





