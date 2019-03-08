def pre_trans(arr,size,direction):
    # 오른쪽
    if direction == 'right':
        for i in range(size):
            arr[i].reverse()
    # 위
    if direction == 'up':
        arr=list(map(list,zip(*arr)))
        arr.reverse()
    # 아래
    if direction == 'down':
        arr=list(map(list,zip(*arr)))
        for i in range(size):
            arr[i].reverse()
    return arr



# 0없애기... ?
def delete_zero(arr,size):
    for i in range(size):
        zero=arr[i].count(0)
        for j in range(zero):
            arr[i].remove(0)
            arr[i]+=[0]

# 계산하기
def cal(arr,size):
    for i in range(size):
        x=0
        while True:
            if x==size-1:
                break
            else:
                if arr[i][x]==arr[i][x+1]:
                    arr[i][x]*=2
                    arr[i].pop(x+1)
                    arr[i]+=[0]
                x+=1
    return arr


# 계산후
def post_trans(arr,size,direction):
    # 오른쪽
    if direction == 'right':
        for i in range(size):
            arr[i].reverse()

    # 위
    if direction == 'up':
        arr = list(map(list,zip(*arr)))
        for i in range(size):
            arr[i].reverse()

    # 아래
    if direction == 'down':
        arr = list(map(list,zip(*arr)))
        arr.reverse()

    return arr


import sys
sys.stdin = open('hw3.txt','r')

for i in range(int(input())):
    a,b=input().split()
    a=int(a)
    pan=[list(map(int,input().split())) for j in range(a)]


    if b!='left':
        pan=pre_trans(pan,a,b)


    delete_zero(pan, a)
    cal(pan, a)

    if b!='left':
        pan=post_trans(pan, a, b)

    print('#{}'.format(i+1))
    for i in range(a):
        print(*pan[i])