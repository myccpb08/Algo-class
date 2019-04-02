import sys
sys.stdin = open('장난감.txt','r')


from collections import defaultdict
n=int(input())  # 완제품번호
m=int(input()) # 관계수

# x,y,k : 중간부품이나 완제품 x 를 만드는 데, 부품 y 가 k 개 필요하다
d = defaultdict(lambda:{})
for i in range(m):
    x,y,k=map(int,input().split())
    d[x].update({y:k})

c = set(i for i in range(1,n+1))-set(d.keys())  # 기본키
data = [0]*(n+1)
for j in d[n].keys():  # 7 일 때, j = 4,5,6
    if j in c: # 기본 키면 4
        data[j]+=d[i][j]
    else:  # 기본 키가 아니면, j=5,6 이면


print(data)

