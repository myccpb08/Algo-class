import sys
sys.stdin = open('hw4.txt','r')

def trans(arr,size):
    new = [[0] * size for j in range(size)]
    for y in range(size):
        for x in range(size):
            new[y][x] = arr[size - x - 1][y]
    return new

for i in range(int(input())):
    size=int(input())
    data=[input().split() for j in range(size)]
    rotation=[]

    #90도 회전 행렬 반환
    a=trans(data,size)
    rotation+=a
    #180도 회전 행렬 반환
    b=trans(a,size)
    rotation+=b
    #270도 회전 행렬 반환
    c=trans(b,size)
    rotation+=c

    print('#{}'.format(i+1))
    for j in range(size):
         print(''.join(rotation[j]), ''.join(rotation[j+size]), ''.join(rotation[j+2*size]), end=' ')
         print()