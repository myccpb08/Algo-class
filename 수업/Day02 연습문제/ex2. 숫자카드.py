import sys
sys.stdin = open('ex2.txt', 'r')

for i in range(int(input())):
    length = int(input())
    number = list(map(int, list(input())))
    start = [0]*(max(number)+1)

    for j in number:
        start[j] += 1

    maxx = start[0]

    for k in range(len(start)):
        if start[k] >= maxx :
            maxx = start[k]
            location = k

    print(f'#{i+1} {location} {maxx}')