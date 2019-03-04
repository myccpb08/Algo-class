# 파이테이블 만들기
l=int(input())
pattern=input()

length = len(pattern)

pi_table = [ -1 if i==0 else 0 for i in range(length+1)]

i=0
for j in range(1, length):
    if pattern[i]==pattern[j]:  # 둘이 패턴이 맞으면
        pi_table[j+1]=pi_table[j]+1
        i+=1

    elif pattern[0]==pattern[j]:  # 둘은 안 맞지만, 처음과 같다
        pi_table[j+1]=1
        i=1

    else:
        pi_table[j+1]=0
        i=0


print(pi_table)
cand = []
for i in range(length+1):
    cand += [i-pi_table[i]]

print(max(cand))

