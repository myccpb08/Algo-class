import sys
sys.stdin = open('단조증가.txt', 'r')


from itertools import combinations
for i in range(int(input())):
    n=int(input())
    print('#{} \n1'.format(i+1))
    if n==1:
          pass
    else:
          for j in range(1,n):
            for k in range(j+1):
                print(len(list(combinations([i for i in range(j)], k))),end=' ')
            print()