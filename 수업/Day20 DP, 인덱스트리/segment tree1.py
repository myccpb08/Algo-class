# ppt 8-14쪽
import sys
sys.stdin = open('input.txt')

IDT = [0]*(1<<4)
Data = list(map(int,input().split()))
howmany = len(Data)

base = 1
while base <= howmany:
    base <<=1   # base = 8   ( base = base<<1 과 동치)

for now in range(base, howmany+base):
    IDT[now] = Data.pop(0)   # 인덱스 8-12에, 9 8 1 7 2 삽입

for parent in range(base-1, 0, -1):
    IDT[parent] = IDT[parent*2] + IDT[parent*2+1]

# 15쪽
#  정리 다 한 트리에서, 인덱스 10번(base로부터 3)의 수를 1→ 5로 바꾸기
def update(a,b):  # 3,5
    where = base + a -1
    IDT[where] = b
    where >>= 1  # 자료 바꾸고 부모님 값도 바꿔야 하니까, 1/2 함

    while  where:
        IDT[where] = IDT[where*2] + IDT[where*2 +1]
        where >>= 1

update(3,5)
print(IDT)

# 17쪽
# 구간합 ( 인덱스 9,10,11,12 의 합을 구하고 싶다 = base 기준으로는 2,3,4,5 의 합)
# 10과 11은 한 부모의 형제이므로, 이 둘의 합은 인덱스 5번 값과 같다
# 즉 원하는 값은, 인덱스 9 + 5 + 12 의 합이다

# 👀 쉬운 버전 : 인덱스가 깔끔하게 1-4 일 때
def RSQ(ffrom, to):  # 1,4  # base 기준으로 1부터 4까지의 합을 구하고 싶다
    ffrom = ffrom + base -1  # 8 ( base 기준으로 인덱스 1)
    to = to + base -1 # 11 ( base 기준으로 인덱스 4)
    sum = 0

    while ffrom < to:
        ffrom >>=1  # ffrom 과  to의 부모 찾아가기
        to >>= 1

    if ffrom == to:  # 최종 부모에 도착하면
        sum = IDT[ffrom]  # 그 값이 구간합
    print(sum)

RSQ(1,4)


# 👀 심화 버전 : 인덱스가 지저분할 때
def RSQ2(ffrom, to):  # 2,5
    ffrom = ffrom + base -1  # 9
    to = to + base -1 # 12
    sum = 0

    while ffrom < to:
        if ffrom&1 :  # 출발 인덱스가 홀수면 ( = 짝이 안 맞다)
            sum+=IDT[ffrom] # 자기 자신을 일단 더하고 (자기는 혼자니까)
            ffrom += 1 # 한 칸 옆으로 이동한다

        if to&1==0:  # 도착 인덱스가 짝수이면 (= 짝이 안 맞다
            sum += IDT[to]
            to -= 1  # 한 칸 앞으로 당긴다

        ffrom >>=1  # ffrom 과  to의 부모 찾아가기
        to >>= 1

    if ffrom == to:  # 최종 부모에 도착하면
        sum += IDT[ffrom]  # 그 값이 구간합
    print(sum)

RSQ2(3,8)

