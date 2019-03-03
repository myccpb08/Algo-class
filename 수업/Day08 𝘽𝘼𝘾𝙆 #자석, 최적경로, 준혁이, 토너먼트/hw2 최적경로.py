import sys
sys.stdin = open('최적경로.txt', 'r')


def road(times, distance, clients, now, visited):  # clients: 고객 몇 명인지 함수에 영향주니까 변수로 넣음
                                                # now : (x,y) 현재 위치 정보가 필요하니까 변수로 넣음
    global temp_min

    if times == clients:  # 고객 방문 다 했으면,
        distance += abs(now[0] - home[0]) + abs(now[1] - home[1])
        if distance <= temp_min:
            temp_min = distance

    else:
        for i in range(clients):
            tmp = 0
            if visited[i] == 0:
                tmp = abs(now[0] - clients_home[i][0]) + abs(now[1] - clients_home[i][1])
                distance += tmp
                visited[i] = 1

                if distance < temp_min:  # 임시 최솟값보다 이미 거리가 커버리면 더 할 필요가 없으니 중단, 작으면 계속
                    road(times + 1, distance, clients, (clients_home[i][0], clients_home[i][1]), visited)

                distance -= tmp
                visited[i] = 0


for k in range(int(input())):
    clients = int(input())
    info = list(map(int,input().split()))
    start = (info[0], info[1])  # 출발지 회사
    home = (info[2], info[3])   # 도착지 집

    clients_home = []
    for j in range(clients):
        clients_home += [(info[2*j+4], info[2*j+5])]

    visited = [0]*clients
    distance = 0
    temp_min = 200*clients

    road(0, 0, clients, start, visited)

    print(f'#{k+1} {temp_min}')

    