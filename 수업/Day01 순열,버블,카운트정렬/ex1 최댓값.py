import sys

sys.stdin = open('input.txt', 'r')  # 파일에서 읽을 때 사용

Data = list(map(int, input().split()))

print(Data)

max_index = -1
max = Data[0]

for now in range(len(Data)):
    if max < Data[now]:
        max = Data[now]
        max_index = now

print(max)
print(max_index+1)



