import sys
sys.stdin = open('ex2.txt', 'r')

def RSQ2(ffrom, to):  # 2,5
    #ffrom = ffrom + base -1  # 9
    #to = to + base -1 # 12
    sum = 0

    while ffrom < to:
        if ffrom&1 :  # 출발 인덱스가 홀수면 ( = 짝이 안 맞다)
            sum+=stree[ffrom] # 자기 자신을 일단 더하고 (자기는 혼자니까)
            ffrom += 1 # 한 칸 옆으로 이동한다

        if to&1==0:  # 도착 인덱스가 짝수이면 (= 짝이 안 맞다
            sum += stree[to]
            to -= 1  # 한 칸 앞으로 당긴다

        ffrom >>=1  # ffrom 과  to의 부모 찾아가기
        to >>= 1

    if ffrom == to:  # 최종 부모에 도착하면
        sum += stree[ffrom]  # 그 값이 구간합
    print(sum)


for tc in range(int(input())):
    have, watch = map(int,input().split())   # 가진 영화수인 have 로 base 를 찾는다
    num = list(map(int,input().split()))

    # base 찾기
    base = 1
    c = 1
    while base <= have:
        base <<= 1   # base 는 해당 레벨에 몇 개의 인덱스를 삽입할 수 있는지 알려주는 숫자
                              # 첫 번째 케이스의 경우, have =3 이니까, base = 4 가 되어야, 영화정보를 담을 수 있다
        c += 1

    # 영화 인덱스 삽입
    stree = [0]*(2**c)
    for i in range(base, base+have):
        #stree[i]=1
        stree[i]=i-base+1

    # 책 권수
    for parent in range(base - 1, 2**(c-2)-1, -1):
        count = 0
        if stree[parent*2]!=0:
            count += 1
        if stree[parent*2+1]!=0:
            count+=1

        stree[parent]=count

    for parent in range(2**(c-2)-1, 0, -1):
        stree[parent] = stree[parent * 2] + stree[parent * 2 + 1]

    print(stree)


    # 영화찾기
    for i in range(watch):
        to_watch = num[i]  # 보고 싶은 영화 번호   # 만약에 보고 싶은 영화가 3번이면, 실제로 영화 위치는 (base + to_watch -1)

        #part =


        # 빼내야 하는 영화 수는  base 부터  [base + to_watch -2] 까지의 구간합
        RSQ2(base, base+to_watch-2)

        # 한 번 하고, 인덱스 이동시켜야 함
