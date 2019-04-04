for t in range(int(input())):
    print('#{}'.format(t + 1),end=' ')
    v,e,a,b=map(int,input().split())
    data = list(map(int,input().split()))
    fam = {i:[] for i in range(1,v+1)}
    for i in range(e):
        fam[data[2*i]]+=[data[2*i+1]]

    a2, b2 = a, b
    a_ = []
    while True:
        if a2==1:
            break
        for j in range(1,v+1):
            if a2 in fam[j]:
                a_ += [j]
                a2= j
                break

    while True:
        if b2 in a_:
            print(b2,end=' ')
            break
        else:
            for j in range(1, v + 1):
                if b2 in fam[j]:
                    b2 = j
                    break

    que = [b2]
    done = []
    while que:
        start = que.pop(0)
        done += [start]
        for i in fam[start]:
            if i not in que and i not in done:
                que+=[i]

    print(len(done),end='\n')