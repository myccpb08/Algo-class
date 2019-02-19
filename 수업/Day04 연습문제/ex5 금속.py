import sys
sys.stdin = open('ex5.txt', 'r')

for t in range(int(input())):
    screws = int(input())  # 나사 수
    thick = list(map(int, input().split()))  # 짝수 인덱스 = 수, 홀수 인덱스 = 암
    head = [thick[i] for i in range(0, 2*screws, 2)]
    tail = [thick[i+1] for i in range(0, 2*screws, 2)]
    a = []

    for j in head:
        if j in tail:
            a += [j]
    for k in a:
        head.pop(head.index(k))
        tail.pop(tail.index(k))

    start = head[0]
    end = tail[0]

    screw_set = []

    for j in range(0, 2 * screws, 2):
        screw_set += [(thick[j:j + 2])]

    order = []

    while len(order) < 2*screws:
        for k in range(screws):
            if screw_set[k][0] == start:
                order += [screw_set[k][0], screw_set[k][1]]
                start = screw_set[k][1]
                break
    print(f'#{t+1}', end=' ')
    for i in order:
        print(i, end=' ')

    print()
