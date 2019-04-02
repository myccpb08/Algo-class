import sys
sys.stdin = open('ex2.txt', 'r')

for tc in range(int(input())):
    student, friends = map(int,input().split())
    data = list(map(int,input().split()))   # 친구 정보
    group = [i for i in range(student+1)]  # 그룹 정보
    visite2 = [0]*(student+1) # 선택 됐는지 안 됐는지

    for i in range(0,len(data),2):
        if visite2[data[i+1]]==1:    # 수신자가 이전에 찍힌적이 있으면   # 1 2 5 4 4 1
            data[i+1], data[i] = data[i], data[i+1]  # 자리 교환
        if

        group[data[i+1]]=group[data[i]]   # 수신자 정보를 발신자로 바꿈
        visite2[data[i+1]]=visite2[data[i]] = 1   # 수신자, 발신자 모두 정보 찍혔다고 바꿈
    print(group)
    print('#{} {}'.format(tc+1,len(set(group))-1))