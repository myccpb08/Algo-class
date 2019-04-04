import sys
sys.stdin=open('정사각형.txt','r')

for i in range(int(input())):
    num,chance=input().split()
    num=[num]  # 32888
    for t in range(int(chance)): # 2번 돌린다면
        result=set([])
        for num_ in num:
            for j in range(len(num_)-1):
                for k in range(j+1,len(num_)):  # j번째와, k 번째 요소 교환
                    if num_[j]==num_[k]:
                        temp=num_
                    else:
                        temp=num_[:j]+num_[k]+num_[j+1:k]+num_[j]+num_[k+1:]
                    result.add(temp)
        num=list(result)

    print('#{} {}'.format(i+1,max(list(map(int,num)))))



