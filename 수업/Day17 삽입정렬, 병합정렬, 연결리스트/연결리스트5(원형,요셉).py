# p354

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

# 죽이는 함수 ( 3번 6번 9번 ... 죽임)
def dead():
    global head
    if head.link.link == head:  # 2명만 남으면 원형리스트에서   "사람1(p)-사람2-사람1(p)" 이니까
        print(head.data)  # 사람1 정보 출력
        print(head.link.data)  # 사람2 정보 출력
        return False

    else:
        pre = head.link  # 사람1(p)-사람2(pre)-사람3(죽을애)-사람4(다음 p 될 애 = next_p)
        next_p = head.link.link.link
        pre.link = next_p  # ( 사람2와 사람 4를 연결시켜줌)
        head = next_p  # head 를 옮기는 게 핵심 ㅋㅋ
        return True

# 41명 연결리스트 만들기
head=None
for i in range(1,42):
    Enqueue(i)

p=head
while p.link:
    p=p.link
p.link=head


# 죽이기
while dead(): 
    pass





