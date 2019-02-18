import sys
sys.stdin = open("ex2.txt", "r")

arr = list(map(int, input().split()))

n = len(arr)

for i in range(1<<n):  # 1<<n : 부분집합의 개수
    result = []
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1<<j):  # i의 j번째 비트가 1이면 j번째 원소를 출력
            result += [arr[j]]
            #print(arr[j], end=', ')
    if sum(result) == 0 and len(result)==3:
        print(result)



print()
