equation = '3+(4+5)*6+7'

stack = []
result = []

isp = {')':-1,
       '*':2,
       '/':2,
       '+':1,
       '-':1,
       '(':0}

icp = {')':4,
       '*':2,
       '/':2,
       '+':1,
       '-':1,
       '(':3}

# 토큰이 연산자면 스택 top 과 비교하여, 높으면 스택에 append
# 여는괄호는 무조건 스택에 append

for i in equation:
    if i.isnumeric():  # 숫자가 들어오면
        result += [i]  # 무조건 결과값 출력

    elif i == '(':   # 여는 괄호가 들어오면
        stack += [i]   # 무조건 스택에 넣는다

    elif i == ')':  # 닫힌 괄호가 들어오면
        while stack[-1] != '(':  # 여는 괄호를 만날 때까지
            result += [stack.pop()]  # stack 을 pop 하여 결과값으로 보낸다
        stack.pop()  # 여는 괄호 만나면 pop 해서 없앤다


    else: # 연산자가 들어오면
        if len(stack) ==0:
            stack += [i]



        else:
            isp_value = isp[stack[-1]]  # 스택 top 의 isp 순위
            icp_value = icp[i]  # 들어온 연산자의 icp 순위
            if icp_value > isp_value:  # 들어올 연산자의 순위가 더 높으면
                stack += [i]   # 연산자를 스택에 넣는다

            else:  # 들어올 연산자의 순위가, 같거나 낮으면,  들어오는 게 이길 때까지 pop
                while isp[stack[-1]] >= icp[i]:
                    result += [stack.pop()]
                stack += [i]

print(result)




