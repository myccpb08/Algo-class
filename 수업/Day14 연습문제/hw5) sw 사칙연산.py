import sys
sys.stdin = open('단조증가.txt', 'r')

for i in range(1,11):
    m=int(input())
    v=[0]*(m+1)
    for j in range(1,m+1):
        v[j]=input().split()


    # 부호면 자식이 있고, 부호아니면, 자식 없다
    def answer(t):
        if v[t][1]=='-':
            return answer(int(v[t][2]))-answer(int(v[t][3]))
        elif v[t][1]=='+':
            return answer(int(v[t][2]))+answer(int(v[t][3]))
        elif v[t][1]=='/':
            return answer(int(v[t][2]))/answer(int(v[t][3]))
        elif v[t][1]=='*':
            return answer(int(v[t][2]))*answer(int(v[t][3]))
        else:  # 자식 없는 애면
            return int(v[t][1])

    print('#{} {}'.format(i,int(answer(1))))




#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2





