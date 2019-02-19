import sys

sys.stdin = open('input1.txt', 'r')

box = list(map(int, input().split()))

now = 0
jumpcnt = 8
size = len(box)
max = 0

for now in range(size):
    jumpcnt = size-now-1
    for next in range(now+1, size):
        if box[next] >= box[now]:
            jumpcnt -= 1
        if jumpcnt > max:
            max += jumpcnt
print(max)
