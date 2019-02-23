for i in range(int(input())):

    p = input()
    stack = []
    for j in p:  # 입력받은 p의 요소에 대하여
        if not len(stack) or j != stack[-1]:  # stack 이 비었있거나,
                                              # 안 비었지만 들어오는 요소가 삭제 안 되면
            stack += [j]  # 쌓는다

        else:
            stack.pop()  # 짝 요소를 삭제한다

    print(f'#{i+1} {len(stack)}')
