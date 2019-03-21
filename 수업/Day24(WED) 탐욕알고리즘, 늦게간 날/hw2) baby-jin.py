# 교재 84p

def baby(cand):
    cand1=cand[0:3]
    cand2=cand[3:6]
    if cand1[0]==cand1[1]==cand1[2] and cand2[0]==cand2[1]==cand2[2] :  # 트리플 2개
        return 'baby-jin'
    elif cand1[0]==cand1[1]==cand1[2] and cand2[0]==cand2[1]-1==cand2[2]-2:  # run 1개 트리플 1개
        return 'baby-jin'
    elif cand2[0]==cand2[1]==cand2[2] and cand1[0]==cand1[1]-1==cand1[2]-2:  # run 1개 트리플 1개
        return 'baby-jin'
    elif cand1[0]==cand1[1]-1==cand1[2]-2 and cand2[0]==cand2[1]-1==cand2[2]-2:  # run 2개
        return 'baby-jin'
    else:
        return '아니야'


data=[0,5,4,0,6,0]
result = []
for i in range(len(data)):  #1
    for j in range(len(data)):  #2
        if i!=j:
            for k in range(len(data)):  #3
                if i!=k and j!=k:
                    for m in range(len(data)):  #4
                        if i!=m and j!=m and k!=m:
                            for x in range(len(data)): #5
                                if i!=x and j!=x and k!=x and m!=x:
                                    for y in range(len(data)):  #6
                                        if i!=y and j!=y and k!=y and m!=y and x!=y:
                                            part = [data[i],data[j],data[k],data[m],data[x],data[y]]
                                            if part not in result:
                                                result.append(part)

print(result)

for i in range(len(result)):
    if baby(result[i])=='baby-jin':
        print('baby-jin')
        break
    if i==len(result)-1:
        print('아니야')




