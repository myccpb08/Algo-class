# 5C3 = 10가지 출력

data = [1,2,3,4,5]

for x in range(len(data)):
    for y in range(x+1,len(data)):
        for z in range(y+1,len(data)):
            print(data[x],data[y],data[z])



# 5H3 = 35가지 출력
print('중복조합')
for x in range(len(data)):
    for y in range(x,len(data)):
        for z in range(y,len(data)):
            print(data[x],data[y],data[z])


