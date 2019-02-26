n=9
que = []
for i in range(41):
    que += [i+1]


n=len(que)
front = -1
rear = -1

while len(que)!=2:
    front += 3
    que.pop((front)%len(que))
    front = (front)%(len(que)+1)-1

print(que)


