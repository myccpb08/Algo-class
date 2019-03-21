data = [1,2,3]
visited = [0]*3
result = [0]*3

# 순열
def getsome(depth):  # depth = 0
    if depth==3:  # 순서 다 정했으니
        print(result)  # result 를 출력
        return

    for i in range(3):
        if not visited[i]:  #방문하지 않았으면
            visited[i] = True  # 방문하고
            result[depth]=data[i]  # result 인덱스에 데이터값 입력
            getsome(depth+1)
            visited[i]=False

getsome(0)
print('\n')

# 중복순열은 재방문 가능하므로 visited 만 없애면 됨
data = [1,2,3]
result = [0]*3

def getsome2(depth):  # depth = 0
    if depth==3:  # 순서 다 정했으니
        print(result)  # result 를 출력
        return

    for i in range(3):
        result[depth]=data[i]  # result 인덱스에 데이터값 입력
        getsome2(depth+1)

getsome2(0)