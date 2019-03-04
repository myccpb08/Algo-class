# Fire = 3  # 화덕 수 그러므로, 0 1 2 번 피자 얹음 == 큐에  0 1 2 넣음
# howmany = 5  # 전체 피자 수
# nextPizza = 3  # 인덱스 3번

import sys
sys.stdin = open('pizza.txt', 'r')

### 전체 풀이

for tc in range(1,int(input())):
    fire, howmany = map(int,input().split())
    print("#%d" %tc, end=' ')

    pizza = list(map(int,input().split()))
    que = []

    for baking in range(fire):
        que.append(baking)
    nextPizza = fire  # 처음에, 다음 피자 번호는 화덕 수와 같다

    while que:
        now = que.pop(0)  # 확인 하려고 지금 꺼낸 피자
        if pizza[now]//2!=0:  # 다 안구어졌다면
            pizza[now] = pizza[now]//2   # 치즈 반으로 녹이고
            que.append(now)  # 다시 큐에 넣음

        elif nextPizza < howmany:   # 다 녹고, nextPizza의 인덱스가 피자 개수보다 적으면
            que.append(nextPizza)
            nextPizza += 1  # 다음 피자 넣어주고, 넣어야 할 피자 index는 1 올려줌
    print(now+1)
