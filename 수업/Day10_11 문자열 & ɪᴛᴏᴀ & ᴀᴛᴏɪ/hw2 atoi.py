# A의 아스키 코드 :  65
# 16진수에서,  10=A, 11=B, 12=C, 13=D, 14=E, 15=F

number = ['4', '2', 'F', 'B']
count = len(number)

for i in range(count):     # for i in number 로 바로 하거나...
    if '0' <= number[i] <= '9':   # 문자도 부등호가 된다고 한다. 대박...
        number[i] = ord(number[i])-ord('0')
    else:
        number[i] =ord(number[i]) -  ord('A') + 10

print(number)