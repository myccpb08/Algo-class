count = 0
for x in range(1,99):
    for y in range(x,99):
        for z in range(y,99):
            if x+y+z==100:
                count += 1
                print((x,y,z), end= ' ')
print()
print(count)

visited = [[[0]*100 for _ in range(100)] for j in range(100)]
count = 0
def getsome(a,b,c):
    global count
    if a+b+c>100:
        return
    if a>b or b>c:
        return
    if a+b+c == 100:
        count += 1
        return
    if visited[a+1][b][c]==False:
        visited[a+1][b][c]=True
        getsome(a+1,b,c)
    if visited[a][b+1][c]==False:
        visited[a][b+1][c]=True
        getsome(a,b+1,c)
    if visited[a][b][c+1]==False:
        visited[a][b][c+1]=True
        getsome(a,b,c+1)

getsome(1,1,1)
print(count)