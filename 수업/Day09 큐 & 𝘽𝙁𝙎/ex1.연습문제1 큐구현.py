Queue = [0]*10
front = -1
rear = -1

# 집어 넣을 때
rear +=1
Queue[rear]=1
rear +=1
Queue[rear]=2
rear +=1
Queue[rear]=3

# 뽑을 때
while front!=rear:  # 둘이 같지 않은 동안
    front += 1
    print(Queue[front])
