data=[1,3,5,6,8]

def odd(data):
    length=len(data)
    mini=[]
    for i in range(0,len(data),2):
        odd_sum = 0
        origin = data[::]
        del origin[i]
        for j in range(0,len(data)-1,2):
            odd_sum += origin[j+1]-origin[j]
        mini += [odd_sum]
    return min(mini)

print(odd([1,3,5,6,8]))