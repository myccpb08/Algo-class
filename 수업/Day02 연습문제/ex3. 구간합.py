import sys
sys.stdin = open('ex3.txt', 'r')

for i in range(int(input())):
    length, group = list(map(int, input().split()))

    numbers = list(map(int, input().split()))

    value = []
    for j in range(length-group+1):
        groups = numbers[j:j+group]

        sum=0
        for k in groups:
            sum+=k
        value+=[sum]

    print(f'#{i+1} {max(value)-min(value)}')


