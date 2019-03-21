import sys
sys.stdin = open('ex5.txt','r')

for tc in range(int(input())):
    print('#{}'.format(tc+1), end=' ')
    data = list(map(int,input().split()))
    A = data[0:12:2]
    B = data[1:12:2]

    compare = []
    for k in [A,B]:
        flag=0
        for i in range(2,6):
            data = sorted(k[:i+1])
            for x in range(len(data)):
                if data.count(data[x])>=3:
                    flag=1
                    compare += [i]
                    break

            data = sorted(list(set(k[:i + 1])))
            if len(data)>=3:
                for j in range(len(data)-2):
                    if data[j]==data[j+1]-1==data[j+2]-2:
                        compare += [i]
                        flag=1
                        break
            if flag==1:
                 break
        if flag==0:
            compare += [7]

    if compare[0]==compare[1]==7:
        print(0)
    elif compare[0]<=compare[1]:
        print(1)
    elif compare[0]>compare[1]:
        print(2)











