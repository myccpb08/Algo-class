import sys
sys.stdin = open("snail.txt", 'r')

grid = [ list(map(int, input().split())) for i in range(5)]  # 입력받아서 5*5 행렬 만듦

reset = []

for i in range(5): # 입력받은 값을 하나의 리스트에 넣어서, 정렬 시킴
        reset+=grid[i]
reset.sort()

grid = [ [0]*5 for i in range(5)]   # grid 초기화 시킴



def region(x,y):
    if 0 <= x < 5 and 0 <= y < 5:
        return True    # 그냥 이 식은 5 5 4 4 3 3 으로 줄어드는 걸 반영 못 함 : x줄 y줄 x 줄 y줄

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]  # 오른쪽 아래 왼쪽 위로

y, x, j, value = 0, -1, 0, 0 # (x,y) = 초기 좌표, value = reset 리스트의 인덱스

while value < 25:
        y += dy[j % 4]
        x += dx[j %4]
        if region(x,y) == True and grid[y][x] == 0:
                grid[y][x]=reset[value]
                value += 1
        else:
                y -= dy[j %4]
                x -= dx[j %4]
                j += 1
for i in range(5):
    print(*grid[i])