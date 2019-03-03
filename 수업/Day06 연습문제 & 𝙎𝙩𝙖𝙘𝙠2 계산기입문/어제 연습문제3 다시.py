# 재귀말고, 노가다로

#a에서 출발 : 1) visit에 반영해주고, 2) 자식이 돌아올 곳을 알려줘야 해서 a를 스택에 저장
#엄마에게 돌아갈 때, pop 해서 돌아감

import sys
sys.stdin = open('input.txt', 'r')

# 많이 쓰는 것들은 global 로 빼두기

MyMap = [[0]*8 for i in range(8)]
stack = [0]*10
visited = [0]*8
top -= 1  # top 만 -1 로 바꾸면, 스택 초기화 가능

def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top == -1:
        return 0
    x = stack[top]
    top -= 1
    return x


def findnext(here):
    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            return next


def DFS(here):
    global top
    print(here)
    visited[here] = True

    while here:  # here 가 있는 동안 실행해라
        next = findnext(here)
        if next:  # 자손이 존재 하면
            push(here)   # stack 에 넣어라. 자식이 없으면 안 넣어줘도 됨
        while next:   # 자식이 있는 동안
            here = next  # 자식으로 이동을 반복 해
            print(here)  # 자식에 도착하면, 도착했다고 print
            visited[here] = True  # 방문했다고 기록
            next = findnext(here)
            push(here)
        here = pop()   # 쭉 가다가 더이상 자식이 없으면 pop 으로 돌아갈 곳
        # 계속 반복하다가, here 가 더이상 존재하지 않으면, while 문이 끝난다

Data = list(map(int,input().split()))
howmany = int(len(Data)/2)

for i in range(howmany):
    start = Data[i*2]
    stop = Data[i*2-1]
    MyMap[start][stop] =1
    MyMap[stop][start] =1

DFS(1)

# 이것도 다시 직접 손으로 해볼 것