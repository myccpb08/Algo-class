import sys
sys.stdin = open('hw1.txt','r')

for tc in range(int(input())):
    length = int(input())
    data = [0] + list(map(int,input().split()))
    tree = [0]*(length+1)

    tree[1] = data[1]

    for i in range(2, length+1):

        tree[i] = data[i]
        while True:
            if i==1:
                break

            elif data[i] < tree[i//2] : # 작으면
                tree[i//2], tree[i] = data[i], tree[i//2]  # 트리의 부모자리에, 들어온 애를 넣어주고, 트리엔 원래부모인 애를 넣음
                i = i//2

            else:
                break




    answer = 0

    while True:
        if i==1:
            break
        else:
            answer += tree[i//2]
            i = i//2
    print(tree)
    print("#{} {}".format(tc+1,answer))



