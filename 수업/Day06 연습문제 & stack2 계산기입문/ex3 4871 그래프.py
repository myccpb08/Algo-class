import sys
sys.stdin = open('input.txt', 'r')



for i in range(int(input())):
    node, path = map(int, input().split())  # node 개수, path 개수

    # 길 정보 받아오기
    road = { i : [] for i in range(1,node+1)}

    for j in range(path):  # path 개수만큼 정보 입력받기
        start, end = map(int, input().split())
        if not start in road:
            road[start] = [end]
        else:
            road[start] += [end]

    start, want_end = map(int,input().split())

    # 방명록 만들기
    guest_book = [0]*(node+1)  # node 개수 +1 만큼 방명록  칸 만들어 놓음

    guest_book[start] = 1  # start 는 무조건 방문하니까, guest_book 을 1로 만듦
    count = 1

    while len(road[start]) != 0 and not want_end in road[start] and count <= path:  # start 에서 갈 수 있는 목적지에, 최종목적지가 없는 동안 반복하고 횟수 5회 이하
        for j in road[start]:
            if guest_book[j] == 0:  # 방문하지 않은 곳이면:
                start = j
                guest_book[j] = 1   # 가서 방문했다고 표시하고
                count += 1
            if len(road[start]) ==0:
                pass





    if len(road[start]) == 0:
        print(f'#{i + 1} 0')
    elif want_end in road[start]:
        print(f'#{i + 1} 1')
    else:
        print(f'#{i + 1} 0')
