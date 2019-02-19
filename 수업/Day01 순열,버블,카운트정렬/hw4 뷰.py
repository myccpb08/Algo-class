for i in range(10):
    t=int(input())
    b=list(map(int,input().split()))
    v=0
    for j in range(t-4):
        p=b[j:j+5]
        v+=max(p.pop(2)-max(p),0)
    print(f'#{i+1} {v}')