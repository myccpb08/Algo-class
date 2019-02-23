import sys
sys.stdin = open('03 input.txt', 'r')  # 파일에서 읽을 때 사용

MyMap = [[0]*8 for i in range(8)]
visited = [0]*8

def DFS(here):
    print(here)   # 도착지점 출력
    visited[here] = True  # 방문했었다는 표시

    # 다음 갈 곳 찾기
    for next in range(8):
        if MyMap[here][next] == 1 and not visited[next]:  # 길이 있고 방문한 적이 없다면
            DFS(next)   # 이제 next 가 here 이 되어 다시 함수가 돌아간다


Data = list(map(int, input().split()))   # 연결된 길 정보 받아 옴
howmany = int(len(Data)/2)   # 세트로 받아오니까 절반만 반복문 돌리면 됨

for i in range(howmany):
    start = Data[i*2]
    stop = Data[i*2-1]
    MyMap[start][stop] =1   # 길 있다고 표시
    MyMap[stop][start] =1

DFS(1)