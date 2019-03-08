import sys
sys.stdin = open('hw2.txt','r')

for m in range(int(input())):
    print('#{}'.format(m+1), end=' ')
    s=[input() for i in range(5)]
    for i in range(max([len(i) for i in s])):
        for k in s:
            try:
                print(k[i],end='')
            except IndexError:
                pass
    print()