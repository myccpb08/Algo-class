import sys
sys.stdin = open('점심시간.txt', 'r')

for t in range(int(input())):
    print('#{}'.format(t+1))
    N=int(input())  # 판 사이즈
    D=[list(map(int,input().split())) for i in range(N)]  # 위치판

    P=[]  # 사람
    S=[]    # 계단
    for y in range(N):
        for x in range(N):
            if D[y][x]==1:
                P+=[(y,x)]
            if D[y][x]>1:
                S+=[(y,x,D[y][x])]

    move = [[0]*len(P) for i in range(len(S))]

    # print(P)
    # print(S)

    for i in range(2):
        for j in range(len(P)):
            move[i][j]=abs(P[j][0]-S[i][0])+abs(P[j][1]-S[i][1])+1+S[i][2]   # 출발하는 시점의 간 + 대기시간 + 각 계단 내려가는 시간

    # print(move)

    first=[]
    second=[]

    for i in range(len(P)):
        if move[0][i] < move[1][i]:  # 첫째계단 이용시간이 짧으면
            first += [(move[0][i], move[1][i])]
        else :
            second += [(move[1][i], move[0][i]) ]


    first.sort(key=lambda x:x[0])
    second.sort(key=lambda x: x[0])


    first2= [ element[0] for element in first]
    print(first2)
    second2 = [ element[0] for element in second]
    print(second2)

    print(first, ' ', second)

    a = max(first2)
    b = max(second2)

    if len(first) > 3:

        pass

    if len(second)>3:
        pass





#1 9
#2 8
#3 9
#4 7
#5 8
#6 8
#7 11
#8 11
#9 18
#10 12

