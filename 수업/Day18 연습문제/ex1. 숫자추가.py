import sys
sys.stdin = open('ex1.txt','r')

# n : 수열의 길이
# m개의 숫자 지정 위치에 삽입
# 인덱스 L의 데이터 출력

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

# 문제
for tc in range(int(input())):
    N, M, L = map(int,input().split())

    numbers = list(map(int,input().split()))

    # 수열 연결
    head = None
    for number in numbers:
        Enqueue(number)

     # 새로운 아이들 삽입
    for i in range(M):
        location, what = map(int,input().split())  # 위치, 무엇을
        newNode = Node(what)
        p=head
        for j in range(location-1):  # 위치로 이동
            p=p.link
        newNode.link = p.link
        p.link = newNode

    # 출력
    p=head
    for i in range(L):
        p=p.link
    print('#{} {}'.format(tc+1,p.data))
