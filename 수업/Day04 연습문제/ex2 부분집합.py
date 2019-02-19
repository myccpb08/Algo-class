import sys
sys.stdin = open('ex2.txt', 'r')

for t in range(int(input())):
    union = [i for i in range(1, 13)]

    how_many, elements_sum = map(int, input().split())

    result = 0
    for i in range(1 << 12):    # 부분집합의 수 = 2의 12승
        subset = []

        for j in range(12):
            if i & (1 << j):    # subset 의 j 번째 수가 1이면 그 수를 출력한다
                subset += [union[j]]
        if sum(subset) == elements_sum and len(subset) == how_many:
                result+=1


    print(f'#{t+1} {result}')

