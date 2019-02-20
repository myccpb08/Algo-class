# 응용. 괄호 세트가 여러 개 일 때 (아스키코드 이용)
stack2 = [0] * 100
top = -1

Info = [-1] * 128  # char = 1byte ,  ASCII code 7bit
Data = '()((<a>{}[])())'

Info[ord(')')] = '('
Info[ord(']')] = '['
Info[ord('>')] = '<'
Info[ord('}')] = '{'

howmany = len(Data)
for i in range(howmany):
    if Data[i] == '(' or Data[i] == '{' or Data[i] == '[' or Data[i] == '<':  # 열린 괄호가 들어오면
        top += 1
        stack2[top] = Data[i]

    elif Info[ord(Data[i])] == stack2[top]:  # 닫힌 괄호가 들어와서 짝이 맞으면
        stack2[top] = 0
        top -= 1

    elif Info[ord(Data[i])] != stack2[top]:  # 닫힌 괄호가 들어와서 짝이 안 맞으면
        top -= 1
        break

if top == -1:
    print('통과입니다')
else:
    print('오류입니다')

