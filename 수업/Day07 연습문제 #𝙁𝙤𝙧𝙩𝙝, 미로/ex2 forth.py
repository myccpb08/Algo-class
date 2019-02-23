import sys
sys.stdin = open('ex2 forth.txt', 'r')

###  나눗셈과, flag 사용법 익히기

for k in range(int(input())):
    flag=True
    equation = list(input().split())
    num_count = 0
    for j in equation:
        if j.isnumeric():
            num_count+=1

    if 2*num_count!=len(equation):
        print(f'#{k+1} error')

    else:  # 계산하는 과정
        stack = []
        for i in range(len(equation)-1):
            i=equation[i]
            if i.isnumeric():
                stack += [i]

            else:
                if len(stack)<2:
                    flag=False
                    break
                else:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    if i == '+':
                        c = b + a
                    elif i == '-':
                        c = b - a
                    elif i == '/':
                        c = b // a   # 나눗셈을 그냥 하면 float 로 들어가서 오류 남
                    else:
                        c = b * a
                    stack += [c]
        if flag:
            print(f'#{k+1} {stack.pop()}')
        else :
            print(f'#{k+1} error')