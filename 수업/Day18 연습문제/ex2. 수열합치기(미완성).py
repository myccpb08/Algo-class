import sys
sys.stdin = open('ex1.txt','r')

# 수열2의 첫 숫자 < 수열1의 숫자 : 수열1의 항들 + 수열2삽입 + 수열1 나머지

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
                                                      # p.link = newNode 이고,

# 문제
for tc in range(int(input())):
    n,m = map(int,input().split())  # n: 수열의 길이, m: 수열의 개수

    first = list(map(int,input().split()))

    # 1번 수열 만들기
    head = None
    for i in first:
        start, end = Enqueue(i)


     # 남은 수열 m-1개
    for i in range(m-1):
        cand = list(map(int,input().split())) # 4 8 7 6

        # 연결할 곳 찾기
        p=head
        while True:
            if p.data<cand[0]:   # 4가 수열의 각 항보다 클동안 반복 ( 수열 중에서 큰 항을 찾아야 하므로)
                p=p.link
            if p.link == None:  # 수열 끝까지 왔다면
                    break
            if p.data>=cand[0]:
                break
            # 맨 앞에 붙일 때 만들어야 함


        # 새로운 수열 꼬리와, 기존 수열 뒷부분
        last = Node(cand[-1])
        last.link = p.link  # 6에 5연결


        for i in range(n-1):
            newNode = Node(cand[i])
            newNode.link = p.link
            p.link = newNode
            p=p.link

        p.link = last




        # 연결하기
        for i in cand:
            newNode = Node(i)
            newNode.link = p.link
            p.link = newNode

        p=head
        while p:
            print(p.data)
            p=p.link

