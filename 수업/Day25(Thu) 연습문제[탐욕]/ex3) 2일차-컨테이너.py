import sys
sys.stdin = open('ex3.txt','r')

for i in range(int(input())):
    container, truck = map(int,input().split())  # 컨테이너수, 트럭 수

    weight = list(reversed(sorted((list(map(int,input().split()))))))# 무거운거 맨 앞
    car_load = list(reversed(sorted(list(map(int,input().split())))))  # 능력 좋은 거 맨 앞


    how = 0
    for j in range(truck):
        for k in range(len(weight)):
            if car_load[j]>=weight[k]:
                how += weight[k]
                weight.pop(k)
                weight = weight[k:]
                break

    print('#{} {}'.format(i+1,how))

