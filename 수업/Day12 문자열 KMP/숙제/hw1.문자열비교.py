import sys
sys.stdin = open('hw1.txt', 'r')

for tc in range(int(input())):
    pattern = input()
    total = input()

    length = len(pattern)  # 패턴 길이
    length2 = len(total)


    # 파이테이블 만들기
    pi_table = [ -1 if i==0 else 0 for i in range(length)]

    i=0
    for j in range(1, length-2):
        if pattern[i]==pattern[j]:  # 둘이 패턴이 맞으면
            pi_table[j+1]=pi_table[j]+1
            i+=1

        elif pattern[0]==pattern[j]:  # 둘은 안 맞지만, 처음과 같다
            pi_table[j+1]=1
            i=1

        else:
            pi_table[j+1]=0
            i=0




    p_a = 0
    t_a = 0
    flag = 0

    while p_a + t_a < length2:
        if pattern[p_a]==total[p_a + t_a]:
            p_a += 1

        else:
            t_a += p_a - pi_table[p_a]
            p_a = 0

        if p_a == length:
            flag = 1
            break

    if flag==1:
        print('#{} 1'.format(tc+1))
    else:
        print('#{} 0'.format(tc+1))