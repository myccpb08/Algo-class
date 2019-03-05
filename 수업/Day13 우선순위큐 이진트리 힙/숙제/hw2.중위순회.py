import sys
sys.stdin = open('hw2.txt', 'r')

def inorder(t):
    global answer
    if 0<t<=n:
        inorder(2*t)
        answer +=data[t]
        inorder(2*t+1)

for i in range(10):
    n=int(input())
    data = [0]*(n+1)
    answer = ''
    for j in range(1,n+1):
        info = input().split()
        data[int(info[0])]=info[1]
    inorder(1)
    print('#{} {}'.format(i+1,answer))