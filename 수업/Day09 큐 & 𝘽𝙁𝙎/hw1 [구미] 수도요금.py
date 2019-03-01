for i in range(int(input())):
    p,q,r,s,w=map(int,input().split())
    b=q
    if w>r:b=q+(w-r)*s
    print(f'#{i+1} {min(p*w,b)}')