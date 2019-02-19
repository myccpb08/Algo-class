Data = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0]*(max(Data)+1)
for i in Data:
    counts[i] += 1

count = [0]*len(counts)
for j in range(0,len(counts)):
    if j==0:
        count[j] = counts[j]
    else:
        count[j] = count[j-1] + counts[j]

count_sort = [0]*(len(Data))

for k in Data:
    count_sort[count[k]-1] = k
    count[k] -= 1

print(count_sort)
