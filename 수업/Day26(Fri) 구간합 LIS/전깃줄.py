import sys
sys.stdin = open('전깃줄.txt', 'r')

line = int(input())
data = []
for i in range(line):
    data+=[tuple(map(int,input().split()))]

data.sort()
end=[]
for i in data:
    end+=[i[1]]

result = [0]*line
result[0]=1
# for i in range(1,line):
#     result[i]=1
#     for j in range(1,i-1):
#         if data[j]<data[i] and 1+result[j]>result[i]:
#             result[i]=1+result[j]
#
# print(result)
#print(end)
for i in range(1,line):
    if end[i-1]<end[i]:  # 증가하는 부분이면
        result[i]= result[i-1]+1
    else:  # 감소하는 부분이면
        temp = 0
        if i==1:
            result[i]=1
        else:
            for j in range(i):
                if end[j]<end[i] and temp<result[j]:
                    temp = result[j]
            result[i]=temp+1
count = 0
for i in result:
    if i==1:
        count+=1
print(count)