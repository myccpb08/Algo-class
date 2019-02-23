for j in range(int(input())):
    
    my_dict = {'}':'{', ')':'('}
    
    s = input()
    stack = []
    arrow = -1
    
    for i in s:
        if i in my_dict.values():  # 열린 괄호가 들어오면
            stack += [i]  # 스택에 넣어라
            arrow += 1  # 화살표 한 칸 up

        elif i in my_dict:  # 닫힌 괄호가 들어오고
            arrow -= 1  # 화살표 한 칸 밑으로 down
            if len(stack) != 0 and stack[-1] == my_dict[i]:  # stack 이 비어있지 않고, stack 의 끝과 짝이 맞으면
                stack.pop()  # 짝을 없앤다
            else:  # stack 이 비었거나, 둘의 짝이 안 맞으면
                break


    if arrow == -1:
        print(f'#{j+1} 1')
    else:
        print(f'#{j + 1} 0')

