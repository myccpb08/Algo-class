# 조합: 5C3
nn = 5
rr = 3
IsUsed= [0]*(rr+1)
def GetSome(n , r):
    if r > rr :
        for i in range(1, rr+1):
              print(IsUsed[i], end=' ')
        print()
        return
    if n > nn :
        return
    IsUsed[r] = n
    GetSome(n, r+1)
    GetSome(n +1, r)

GetSome(1,1)
#

# 순열 : 교훈이꺼
A=[0]*3 ## 출력할 순열
# A=[0,0,0]
DB={}
for i in range(1,6):
    DB.update({i:1}) ## {data : fuel}   # i를 한 개 충전시킨다 ( 한 번 선택될 수 있다는 의미, 중복조합만든다고 3으로 바뀌면, 세 번 선택될 수 있다는 의미)

count=0
def go(now_index):
    global DB
    global count
    if now_index==3:
        print(A)
        count=count+1
        return
    for D in DB.keys():  # DB.keys= 1 2 3 4 5
        if DB[D]>0:  # 들어온 아이템의 연료가 남아있는지 체크
            # 아래 3줄을 추가하면 중복조합
            if now_index>0:
                if A[now_index-1]>D:
                    continue
            A[now_index]=D  # A 순열의 현재 인덱스를 D로 채움
            DB[D]=DB[D]-1 # 연료 소모

            go(now_index+1) #다음 재귀로
            DB[D] = DB[D]+1
go(0)
print(count)