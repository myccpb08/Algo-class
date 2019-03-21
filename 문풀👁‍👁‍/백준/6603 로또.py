def com(k,data):
    for x in range(k):
        for y in range(x+1,k):
            for z in range(y+1,k):
                for m in range(z+1,k):
                    for n in range(m+1,k):
                        for t in range(n+1,k):
                            print(data[x],data[y],data[z],data[m],data[n],data[t])
    print()

for i in range(987654321):
    a=list(map(int,input().split()))
    if a==[0]:
        break
    else:
        k=a[0]
        s=a[1:]
        com(k, s)


