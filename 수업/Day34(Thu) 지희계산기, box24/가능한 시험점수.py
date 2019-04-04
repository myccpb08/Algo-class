import sys
sys.stdin = open('시험점수.txt','r')

for t in range(int(input())):
    n=int(input())  #3
    s=list(map(int,input().split()))   # 2 3 5
    result=[0]   # 다 틀렸을 때
    score=[1]+[0]*100*n   # 100점으로 10개 들어왔을 때 최대 1000점, 0점은 항상 있음

    for i in s:   # 2 3 5
        for j in range(len(result)):
            if score[i+result[j]]==0:
                score[i+result[j]]=1    # 해당 점수가 새롭게 발견되면, 1을 찍는다
                result += [i+result[j]]

    print('#{} {}'.format(t+1,len(result)))