balls=[1,2,3,4]
choice=2
visited = [0]*len(balls)

def com(n,r):

    if r>=choice:  # 공을 다 찾았으면
        for i in range(len(balls)):
            if visited[i]==1:
                print(balls[i], end=' ')
        print()
        return

    if n>=len(balls):  # 더이상 찾을 공이 없음
        return


    visited[n]=1
    com(n+1,r+1)
    visited[n]=0
    com(n+1,r)


com(0,0)





















