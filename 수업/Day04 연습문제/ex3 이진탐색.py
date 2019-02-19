import sys
sys.stdin = open('ex3.txt', 'r')


for i in range(int(input())):
    p, a, b = map(int, input().split())
    c = []
    for k in [a, b]:
        f = p
        count = 0  # 시도 차수
        get_page = 0 # 펼쳐서 나온 페이지
        start = 1
        if k == 1 or k == f:   #  끝페이지거나 시작페이지
            count = 1
        else:
            while get_page != k:
                get_page = int((start + f)/2)
                count += 1
                if k < get_page :
                    f = get_page
                elif k > get_page :
                    start = get_page
                else:
                    break
        c+=[count]   #  A의 시도는 c[0] 에 b의 시도는 c[1] 에 저장

    print(f'#{i+1}', end=' ')
    if c[0]>c[1]:
        print('B')
    elif c[0]<c[1]:
        print('A')
    else:
        print(0)