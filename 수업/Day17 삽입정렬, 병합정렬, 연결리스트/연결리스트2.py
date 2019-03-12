# 382p 문제

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def Enqueue(item):
    global head
    newNode = Node(item)
    if head == None:  # 시작부분이면
        head = newNode  # 머리 설치
    else:
        p = head     # 머리가 있는 상태면
        while p.link:  # link가 존재하지 않는 곳까지 찾아서 내려간 다음에
            p = p.link
        p.link = newNode  # 꼬리를 단다


head = None

Enqueue(1)
Enqueue(5)
Enqueue(2)
Enqueue(4)
Enqueue(3)     #  1-5-2-4-3


p=head
print(p.data)
print(p.link.link.data)
print(p.link.link.link.link.data)
print(p.link.link.link.data)
print(p.link.data)




