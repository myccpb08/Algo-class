import sys
sys.stdin = open('ex1.txt', 'r')

for t in range(int(input())):  # 테스트 케이스 수
    n = int(input()) # 직사각형 개수
    board = [ [0]*10 for i in range(10)] # 10*10 격자판 만들기

    for i in range(n) :  #n번 색깔 겹치기
        x1, y1, x2, y2, color = map(int, input().split())

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if board[x][y] != color:
                    board[x][y] += color

    result = 0
    for y in range(10):
        for x in range(10):
            if board[y][x] == 3:
                result += 1

    print(f'#{t+1} {result}')