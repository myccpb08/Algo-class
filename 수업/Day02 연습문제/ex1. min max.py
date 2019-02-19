import sys
sys.stdin = open('ex1.txt', 'r')

for i in range(int(input())):
    length = int(input())
    numbers = list(map(int, input().split()))

    maxx = mini = numbers[0]
    for j in range(length):
        if numbers[j] > maxx:
            maxx = numbers[j]  # 최댓값 찾기
        if numbers[j] < mini:
            mini = numbers[j]  # 최솟값 찾기

    print(f'#{i+1} {maxx-mini}')