# 기본. 괄호 세트가 1종류 일 때

a = '()()(('
stack = [0]*10
top = -1

for i in range(len(a)):
    if a[i] == '(':    # 열린 괄호인 경우
        top += 1
        stack[top] = a[i]

    else:  # 닫힌 괄호인 경우
        stack.pop(top)
        top -= 1

if top == -1:
    print("통과")
if top != -1:
    print('오류')