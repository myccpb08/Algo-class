def half(start,end):
    if end == start:
        return start
    c=(start+end)//2
    return rsp(half(start,c), half(c+1,end))

def rsp(a,b):
    if info[a-1]==1 and info[b-1]==3:
        return a
    elif info[a-1]==3 and info[b-1]==1:
        return b
    else:
        if info[a-1]>=info[b-1]:
            return a
        else:
            return b
    

for i in range(int(input())): 
    n = int(input())
    info = list(map(int,input().split()))
    print(f'#{i+1}')

    