import sys
sys.stdin = open('ex1.txt', 'r')

def same(y,x,size):  # 한 영역에 대하여, 모두 같은 모양이면 True, 아니면 False
    start = grid[y][x]
    for i in range(size):
        for j in range(size):
            if start!=grid[y+i][x+j]:
                return False
    return True

def getsome(y,x,size):
    global info

    if same(y,x,size)==True or size==1:
        start = grid[y][x]
        info[start]+=1
        return

    else:  # 영역이 다르면 분할
        next = size // 3
        for i in range(3):
            for j in range(3):
                getsome(y + i * next, x + j * next, next)  # 9개 영역 차례대로 탐색


n = int(input())
grid = [list(map(int,input().split())) for i in range(n)]
info = {-1:0, 0:0, 1:0}

getsome(0,0,n)

print(info[-1])
print(info[0])
print(info[1])

