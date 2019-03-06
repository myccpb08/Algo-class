money = 40   # 10 <= money <= 35000
activity = 6   # 1 <= activity <= 21

pay = [7, 13, 17, 19, 29, 31]
visit = [0,0,0,0,0,0]


init_sum = 37  # 7+13+17  : 답은  37<=answer<=40


def budget(sofar):
    global init_sum

    if sofar > 40:
        return # 계산하다가 예산을 초과하면 더이상 할 필요 없음

    if init_sum < sofar:
        init_sum = sofar
        return


    for i in range(len(pay)):
        if visit[i]==0:
            visit[i]=1
            sofar += pay[i]
            budget(sofar)
            visit[i]=0
            sofar -= pay[i]


budget(0) # 현재 금액 0원으로 시작
print(init_sum)