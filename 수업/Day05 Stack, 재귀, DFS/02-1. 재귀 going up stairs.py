def stair(stairs):  # stairs = 계단 수
    if stairs == 1:
        return 1
    elif stairs == 2:
        return 2
    return stair(stairs-1)+stair(stairs-2)

print(stair(5))

# 선생님 풀이

ans = 0

def GetSome(here):
    global ans
    if here == howmany:
        ans += 1
        return
    if here > howmany:
        return 0
    GetSome(here+1)
    GetSome(here+2)

howmany = int(input()) # 몇 층 갈 건지
GetSome(0)
print(ans)