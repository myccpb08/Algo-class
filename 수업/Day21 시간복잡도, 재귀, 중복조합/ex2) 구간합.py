# 문제: 배열에 정수들이 저장되어 있다. 연속된 구간들 중 그 합이 가장 큰 구간의 합을 찾고,
# 해당 구간이 어디부터 어디인지 구하는 알고리즘을 작성하라

data = [5, 1, -4, 2, -1, -5, -2, 8, -3, 6]
rangesum = [0]*len(data)
rangesum[0]=data[0]

for i in range(1,len(data)):
    rangesum[i] = max(rangesum[i-1]+data[i], data[i])
    # if rangesum[i-1]<0:
    #     rangesum[i]=data[i]
    # else:
    #     rangesum[i]=data[i]+rangesum[i-1]
print(max(rangesum))

a=rangesum.index(max(rangesum))  ## 최댓값 찾은거 인덱스
start = 0
for i in range(a, -1, -1):
    if rangesum[i]<0:
        start = i
        break

print(data[start+1 : a+1])

