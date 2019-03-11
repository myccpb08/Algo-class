data = [6,7,9,4,3,1,0]

def merge(left, right):
    global swap
    result = [0]*(len(left)+len(right))
    i = j = k = 0

    while i < len(left) and j <len(right):
        if left[i]<=right[j]:
            result[k]=left[i]
            i = i+1

        else:    # 오른쪽이 작으면   swap 일어남 (( 각각의 박스에서는 이미 정렬되어 있으니까)
            result[k]=right[j]
            swap += len(left)-i
            j = j+1

        k = k+1

    if i < len(left): 
        while i < len(left):
            result[k]=left[i]
            i += 1
            k +=1
    else:
        while j < len(right):
            result[k]=right[j]
            j += 1
            k +=1
    return result


##################################################

def merge_sort(data):

    if len(data) <= 1:
        return data

    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


######

n=input()
data=list(map(int,input().split()))

swap = 0
merge_sort(data)
print(swap)

