import sys
sys.stdin = open('ex1 계산기.txt', 'r')

for k in range(10):
    s,equation = input(), input()
    stack,result,stack2 = [],[],[]
    isp={')': -1,'*': 2,'/': 2,'+': 1,'-': 1,'(': 0}
    icp={')': 4,'*': 2,'/': 2,'+': 1,'-': 1,'(': 3}
    for i in equation:
        if i.isnumeric():
            result += [i]
        elif i == '(':
            stack += [i]
        elif i == ')':
            while stack[-1] != '(':
                result += [stack.pop()]
            stack.pop()
        else:
            if not len(stack):
                stack += [i]
            else:
                if icp[i] > isp[stack[-1]]:
                    stack += [i]
                else:
                    while isp[stack[-1]] >= icp[i]:
                        result += [stack.pop()]
                    stack += [i]
    for i in result:
        if i.isnumeric():
            stack2 += [i]
        else:
            a,b = int(stack2.pop()),int(stack2.pop())
            if i=='+':
                c=b+a
            elif i=='-':
                c=b-a
            elif i=='/':
                c=b//a
            else:
                c=b*a
            stack2+=[c]
    print(f'#{k+1} {stack2.pop()}')