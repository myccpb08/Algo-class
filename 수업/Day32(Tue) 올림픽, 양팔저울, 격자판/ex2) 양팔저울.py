import sys
sys.stdin=open('올림픽.txt','r')

def scale(now,right,left,x):
    if left<right:  # 오른쪽이 왼쪽보다 크면 그만
        return 0
    if now==n: # 추 9개 다 썼으면
        return  1# 경우의 수 한 개
    if memo[x]!=-1:  # 저장된 값이 있으면 더이상 계산하지 않고
        return memo[x]  # memo 된 값을 가져오면 됨

    # 다 아니면 새로운 거 계산
    temp = 0
    for i in range(n):  # 추의 개수
        if used[i]==0:  #추를 사용하지 않았으면
            used[i]=1  # 추 사용하고
            temp += scale(now+1, right, left+w[i], x+(1<<(i)))  # 왼쪽에 더했을 때
            temp += scale(now+1, right+w[i], left, x+(1<<(i+n)))  # 오른쪽에 더했을 때
            used[i]=0

    memo[x]=temp   # 계산다하고 메모에 저장
    return temp  # 계산끝난 경우의 수

for t in range(int(input())):
    n=int(input())  # 추의 개수
    w=list(map(int,input().split()))  # 추의 무게
    used=[0]*n  # 사용한 추에 대한 정보
    memo = [-1]*(1<<n*2)
    cnt = scale(0,0,0,0)   # 사용한 추의 수, 오른쪽무게, 왼쪽무게, 상황에 대한 정보를 어떻게..?

    print('#{} {}'.format(t+1,cnt))