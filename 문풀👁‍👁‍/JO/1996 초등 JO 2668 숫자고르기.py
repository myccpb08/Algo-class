a=int(input())
group={}
for i in range(1,a+1):
    group[i]=int(input())
count=0
result=[]
for i in group:
    x,y = i, group[i]
    closed=[x, y]
    while True:
        if y != closed[0] and closed.count(y)<=2:
            x = y
            y = group[x]
            closed += [x, y]
        else:
            if closed[0]==closed[-1]:
                count+=1
                result+=[closed[0]]
            break
print(count)
for i in result:
    print(i)