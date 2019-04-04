import sys
sys.stdin = open('정사각형.txt', 'r')

# 벡터합 : 반은 더하고, 반은 뺌
def love(nth,plus,minus,Vector_y, Vector_x ):    #( n번째 지렁이  , 더한 횟수, 뺀 횟수, 벡터합 y, 벡터합 x )
    global mymin
    if plus==minus==stop:   # 절반만큼 계산했으면, 최종 벡터임
        temp = (Vector_y)**2+(Vector_x)**2
        if temp<mymin:
            mymin=temp

    if mymin==0:
        return

    else:
        if plus<stop:  # 플러스 횟수가 모자라면
            love(nth+1,plus+1,minus,Vector_y+worm[nth][0],Vector_x+worm[nth][1])
        if minus<stop:  # 마이너스 횟수가 모자라면
            love(nth+1, plus,minus+1,Vector_y-worm[nth][0],Vector_x-worm[nth][1])

for t in range(int(input())):
    n=int(input())
    stop=n//2
    worm=[]
    for i in range(n):
        y,x = map(int,input().split())
        worm += [(y,x)]
    mymin = 80000000000
    love(0, 0, 0, 0,0)

    print('#{} {}'.format(t+1,mymin))