import sys
sys.stdin = open('ex3.txt','r')

class Node:
    def __init__(self, data, link=None, parent=None):
        self.data = data
        self.link = link
        self.parent = parent

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
        newNode.parent = p

def Insert(item):
    newNode = Node(item)
    newNode.link = p.link
    p.link = newNode
    newNode.parent = p


for tc in range(int(input())):
    length,jump,times = map(int,input().split())

    #1. 시작 순열 만들기
    start = list(map(int,input().split()))
    head = None
    for i in start:
        Enqueue(i)


    # 삽입
    p=head
    for time in range(times):
        i=0
        while i!=jump-1:
            if p.link == None:
                p = head
            else:
                p = p.link
            i += 1

        if p.link==None:
            a = head.data
        else:
            a= p.link.data

        if p.link == None:
            newNode = Node(p.data+a)
            p.link = newNode
            p=newNode

        else:
            Insert(p.data+a)
            p = p.link

    # 출력하기
    print('#{}'.format(tc+1), end=' ')
    p=head
    num = []
    while p:
        num += [p.data]
        p=p.link

    num = num[::-1]
    if len(num)>=10:
        print(*num[:10])
    else:
        print(*num)