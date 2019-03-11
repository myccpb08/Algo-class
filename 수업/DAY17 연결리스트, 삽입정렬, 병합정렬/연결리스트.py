class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link
        
node1 = Node(1)       # 이렇게 하면  1+None : 1=data, link = None
node2 = Node(2)       # 이렇게 하면  2+None
node3 = Node(3)       # 이렇게 하면  3+None
node4 = Node(4)       # 이렇게 하면  4+None
node5 = Node(5)       # 이렇게 하면  5+None

node1.link = node2   # 이렇게하면  1+(2+None) : node2 가 node1 의 꼬리에 연결됨
node2.link = node3   # 이렇게하면  1+(2+(3+None))
node3.link = node4
node4.link = node5

head = node1  # 헤드는 움직이면 안 된다. 늘 선발대에 고정 (node1 = Node(1) 인 상태)


# 1-5 출력하기
p = head  # 헤드는 움직이면 안 돼서, 복사본 만들어둠
while p:
    print(p.data)
    p=p.link


# 위 문장과 아래 문장 동일
p=head
print(p.data)
print(p.link.data)
print(p.link.link.data)
print(p.link.link.link.data)
print(p.link.link.link.link.data)



