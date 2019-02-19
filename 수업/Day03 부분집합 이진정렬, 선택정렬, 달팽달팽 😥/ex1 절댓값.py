
import sys
sys.stdin = open("input.txt", "r")

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1

def IsNotWall(y,x):
    if x >=0 and x<5 and y>=0 and y<5:
        return True  # 벽이 아니고 데이터 있는 곳
    else:
        return False  # 아니면 범위 넘어갔음


def Mycalc(a, b):
    if a > b :
        return a-b
    else :
        return b-a



Data = [[0 for i in range(5)] for j in range(5)]

for i in range(5):
    Data[i] = list(map(int, input().split()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
sum = 0

for y in range(5):
    for x in range(5):
        for direction in range(4):  # delta 쓸 때는 for 문 3개
            newY = y+dy[direction]  
            newX = x +dx[direction]   # 상, 하, 좌, 우 순서로 좌표 바뀜

            if IsNotWall(newY, newX):  # 범위 안에 있으면
                sum += Mycalc(Data[y][x], Data[newY][newX])

print(sum)