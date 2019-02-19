grid = [[0]*100 for i in range(100)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1,x2):
        for y in range(y1,y2):
            if grid[x][y]==0:
                grid[x][y]=1
count=0
for x in range(100):
    for y in range(100):
        if grid[x][y]==1:
            count+=1

print(count)