
# -----  ver1 : 파이썬에만 있는 append 와 pop 이용   ----- #

stack = []

for i in range(1, 4):
    stack.append(i)  # stack = [1, 2, 3]

while stack:   # stack 에 원소가 있는 동안
    print(stack.pop())   # pop 해서 마지막 요소를 출력


# -----  ver2 : 다른 언어로 구현 원리   ----- #

stack = [0]*10  # 시험시 10000
top = -1

for i in range(1, 4):
    top += 1
    stack[top] = i

while top != -1:    # top = -1 이면 스택이 빈 거니까
    print(stack[top])
    top -= 1

