# 66p selection sort 재귀

data = [34,10,16,89,54,23,67]

def choice(n):
    if n==len(data)-1:
        return

    min = n
    for j in range(n+1,len(data)):
        if data[j] < data[min]:
            min = j
    data[min], data[n] = data[n], data[min]
    choice(n+1)

choice(0)
print(data)
