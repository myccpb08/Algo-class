import sys
sys.stdin = open('hw1.txt','r')

for i in range(int(input())):
    s=''
    for j in range(int(input())):
        a,b=input().split()
        s+=a*int(b)

    print('#{}'.format(i+1))

    r=len(s)//10

    for j in range(r):
        print(s[10*j:10*(j+1)])

    rest=len(s)-(10*r)

    print(s[-1*rest::])