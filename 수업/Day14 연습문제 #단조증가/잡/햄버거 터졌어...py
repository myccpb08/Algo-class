import sys
sys.stdin = open('햄버거.txt', 'r')


# 같은 재료는 여러번 사용 할 수 없다.

for i in range(int(input())):
    f,c=map(int,input().split())  # 재료종류와 칼로리 정보
    v=[0]*(f+1)
    data=[0]
    for j in range(f):
        data+=[list(map(int,input().split()))]  # [점수, 칼로리]

    myscore=0

    def ham(score,cal):
        global myscore

        if cal>c:  # 현재까지의 합이 주어진 칼로리를 넘어버리면 멈춰
            return

        if score>=myscore:  # 칼로리범위에 맞으면서, 현재 내가 세운 만족값보다 크면
            myscore=score  # 현재가지의 만족값으로 변화

        for j in range(1,f+1):  # 재료 탐색
            if v[j]==0:  # 방문하지 않았으면
                score+=data[j][0]   # 점수 더해주고
                cal+=data[j][1]  # 칼로리 더해주고
                v[j]=1  # 방문했다고 표시
                ham(score,cal)
                v[j]=0
                score-=data[j][0]
                cal-=data[j][1]



    ham(0,0)  # 현재까지의 합이 0인 걸로 시작
    print('#{} {}'.format(i+1,myscore))