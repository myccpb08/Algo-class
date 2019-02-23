equation = '345+6*+7+'

stack = []

# 피연산자를 만나면 스택에 넣는다
# 연산자를 만나면 피연산자를 스택에서 pop 하여 연산, 연산결과를 다시 스택에 sjgsmsek
# 수식이 끝나면 마지막으로 스택을 pop 하여 출력한다

stack = []

for i in equation:
    if i.isnumeric():
        stack += [i]
    else:
        a=int(stack.pop())
        b=int(stack.pop())
        if i == '+':
            c=b+a
        elif i == '-':
            c= b-a
        elif i == '/':
            c= b/a
        else:
            c=b*a
        stack += [c]

print(stack.pop())
