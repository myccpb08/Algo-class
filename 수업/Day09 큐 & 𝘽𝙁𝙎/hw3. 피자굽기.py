import sys
sys.stdin = open('hw3.txt', 'r')

for test in range(int(input())):
    n,m = map(int,input().split())  # n=화덕 크기, m=피자
    cheeze = list(map(int,input().split()))  # 치즈 정보

    rear=-1
    que = [0]*n

    # 피자 화덕에 넣기
    for i in range(n):
        rear += 1
        que[rear] = cheeze[rear]    # que =  치즈양 = [7 2 6]  들어있고,  rear 는 2

    pizza = [i for i in range(1,n+1)]  # pizza = [ 1 2 3 ]   피자 번호 의미

    while True:
        for i in range(n):
                if que[i]!=0:
                    que[i]=que[i]//2  #  한 번 턴 돌 때마다, 치즈 반으로 감소
                    if que[i]==0:   # 만약에 치즈 양이 0이면
                        rear = rear + 1  #  rear +1 하고, 
                        if rear>=m:     #  rear 가  피자 개수를 넘어가면, 더이상 채우지 못하므로, 0으로 둠
                            que[i]=0
                        else:   # 아직 피자를 더 채워야 한다면
                            que[i] = cheeze[rear]   #   rear = 3 이라면,  치즈0된피자자리에,  새로운 피자 투입
                            pizza[i] = rear+1   # 4번 피자가, 2번 피자 자리에 들어오므로, pizza = [ 1 4 3 ] 으로 바뀜
        if rear>=m-1:  #  rear 가  피자수-1 (인덱스라서) 보다 커지면, while 문을 멈춤
            break

    flag =0
    while flag!=1:   #  이제 피자 교체는 다 끝났으므로, 화덕에 남은 피자만으로 , while 문을 돌려서 남은 피자가 1개 될 때까지
        for i in range(n):
            que[i]=que[i]//2
            if que.count(0) == n-1:
                flag=1
                break

    pizza_ing = que.index(max(que))
    print(f'#{test+1} {pizza[pizza_ing]}')