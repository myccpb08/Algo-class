# Start 교재 92p

data =[-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
visited = [0]*10

def getsome(k,sum):
    global count

    if k ==10:
        if sum==0:
            for i in range(10):
                if visited[i]==1:
                    print(data[i], end=' ')
            print()
            count += 1
            return

    if k >= 10:
        return
    else:
        visited[k] = 1
        getsome(k + 1, data[k] + sum)
        visited[k] = 0
        getsome(k + 1, sum)

count = 0
getsome(0,0)

print('총 개수')
print(count)