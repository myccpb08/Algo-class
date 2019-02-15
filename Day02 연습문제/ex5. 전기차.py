import sys
sys.stdin = open('ex5.txt', 'r')

for i in range(int(input())):
    k, n, m = map(int, input().split())           # n : 종점 정류장
                                                                    # k : 한 번 충전으로 이동가능 수
                                                                    # 구할 거, 몇 번 충전? # 설치 이상하면 0

    charging_stop = list(map(int, input().split()))[::-1]  # 충전하는 정류장역순 (m 이 길이)

    start = 0
    answer = 0

    while start + k < n:  # 끝 지점이, 종점 정류장보다 적으면 계속 반복해라   # start + k = 한 번 충전으로 갈 수 있는 최대 위치
        for charging_point in charging_stop:
            if charging_point > start+k:  # 가장 먼 충전소에서 충전을 못 하면
                continue  # 그 다음으로 가까운 충전소를 찾아라

            else:
                if start != charging_point:
                    start = charging_point  # 시작 지점을 재충전한 곳으로 변경하고,
                    answer += 1  # 충전 횟수를 한 번 추가한다
                    break
                else:
                    start = n
                    answer = 0
                    break

    print(f'#{i+1} {answer}')