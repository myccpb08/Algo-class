class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def Enqueue(item):
    global head
    newNode = Node(item)
    if head == None:
        head = newNode
    else:
        p = head
        while p.link!=None:
            if p.link.data > newNode.data:
                newNode.link = p.link   # 이 문장 몰랐음( 1-5 가 연결되어있는 상태에서, 2를 넣으려면,   5를 복사해서 2-5 연결시키고 
                break
            else:
                p=p.link
        p.link = newNode  # 얘를 다시 1-2-5 로 연결한다


# 1-5-2-4-3 연결
head = None

Enqueue(1)
Enqueue(5)
Enqueue(2)
Enqueue(4)
Enqueue(3)


target = head

while target:
    print(target.data)

    target=target.link


