a= [[1,2,3],
    [4,5,6],
    [7,8,9]]

def tr(a):
    for y in range(3):
        for x in range(3):
            if y>x:
                a[y][x],a[x][y]=a[x][y],a[y][x]

tr(a)

print(a)