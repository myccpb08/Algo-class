import sys
sys.stdin = open('hw1.txt','r')

def pq(num):
    while num != 1:
        if tree[num] < tree[num//2]:
            tree[num//2], tree[num] = tree[num], tree[num//2]
            num = num//2
        else:
            break


for tc in range(int(input())):
    length = int(input())
    tree = [0] * (length + 1)
    now = 0


    for i in map(int,input().split()):
        now += 1
        tree[now] = i
        pq(now)


    result = 0

    while True:
        if now == 1:
            break
        else:
            now = now // 2
            result += tree[now]

    print("#{} {}".format(tc+1,result))