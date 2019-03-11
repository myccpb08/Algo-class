import sys
sys.stdin = open('달리기.txt','r')

swap = 0
def merge(left, right):
    global swap, run
    result = [0]*(len(left)+len(right))
    i = j = k = 0

    while i < len(left) and j <len(right):
        if left[i]<=right[j]:
            result[k]=left[i]
            i = i+1

        else:    # 오른쪽이 작으면   swap 일어남 (( 각각의 박스에서는 이미 정렬되어 있으니까)
            result[k]=right[j]
            #swap += len(left)-i
            swap += 1
            run[right[j]]=swap
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

n = int(input())
student = [int(input()) for i in range(n)]
run = { i:0 for i in student}
#
#
#
print(student)
print(merge_sort(student))
print(run)

# for i in range(n):
#     print(merge_sort(student[:i+1]))
#     print(swap)


