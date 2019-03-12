# 연결리스트 만들기
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
        while p.link:
            p = p.link
        p.link = newNode

# Insert 함수
def Insert(item):
    newNode = Node(item)
    newNode.link = p.link
    p.link = newNode

# delete 함수
def delete(p):
    p.link = p.link.link


# change 함수
def change(item):
    global p
    p.data = item



for tc in range(int(input())):
    length, times, where = map(int,input().split())
    numbers = list(map(int,input().split()))

    # numbers로 연결 리스트 만들기
    head = None
    for number in numbers:
        Enqueue(number)

    for time in range(times):
        order = input().split()  # act, place, num
        place = int(order[1])
        act = order[0]

        # 삭제
        if act == 'D':
            p=head
            for i in range(place-1):
                p=p.link
            delete(p)

        if act == 'C':
            p=head
            for i in range(place):
                p=p.link
            change(order[2])

        if act == 'I':
            p=head
            for i in range(place-1):
                p=p.link
            Insert(order[2])

    p=head
    for i in range(where):
        p=p.link

        if i<where-1 and p.link==None:
            print('#{} -1'.format(tc+1))
            break

    if p.data!=None and i==where-1:
        print('#{} {}'.format(tc+1, p.data))




