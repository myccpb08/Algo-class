import sys
sys.setrecursionlimit(100000000)
sys.stdin = open('로또.txt', 'r')

def check2(y,x,visited,info):
    visited[y][x]=1
    for i in range(4):
        new_y, new_x = y+dy[i], x+dx[i]
        if 0<=new_y<v and 0<=new_x<hr and info[new_y][new_x]!=0 and visited[new_y][new_x]==0:
            check2(new_y,new_x, visited, info)


def check(info):
    count = 0
    visited = [[0]*hr for i in range(v)]
    for y in range(1,v-1):
        for x in range(hr):
            if info[y][x]!=0 and visited[y][x]==0:  # 바다가 아니면
                count += 1
                if count <2:
                    check2(y,x,visited,info)
                else:
                    return count
    return count


dx = [-1,1,0,0]
dy = [0,0,1,-1]

v, hr = map(int,input().split())
info = [ list(map(int,input().split())) for i in range(v)]
hour = 0

while check(info)<2:
    if check(info)==0:
        print(0)
    else:
        change=[]
        hour += 1
        for y in range(1,v-1):
            for x in range(hr):
                if info[y][x]>0:  # 빙산이면
                    ice_count = 0  # 주변 얼음을 카운트
                    for i in range(4):  # 빙산 주위 4방향에 대하여
                        new_y, new_x = y+dy[i], x+dx[i]
                        if 0<=new_y<v and 0<=new_x <hr and info[new_y][new_x]==0:
                            ice_count+=1  # 물 수를 카운트
                    info[y][x] -= ice_count  #물 수 만큼 빼고
                    if info[y][x]<=0:  # 그게 바다가 되면
                        change+=[(y,x)] # 좌표를 저장했다가

        for i in change:  # 바꿔줌
            info[i[0]][i[1]]=0

print(hour)