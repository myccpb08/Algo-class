data = [6,7,9,4,3,1,0]

def merge(left, right):
    result = [0]*(len(left)+len(right))
    i = j = k = 0   # i=왼쪽 인덱스,  j = 오른쪽 인덱스, k = result 의 인덱스

    while i < len(left) and j <len(right):  # 양쪽 인덱스의 현재 위치가, 각 리스트의 범위를 넘어가지 않으면
        if left[i]<=right[j]:   # 왼쪽이 오른쪽보다 작으면
            result[k]=left[i]   # result 에 왼쪽 값을 넣고
            i = i+1   # 왼쪽 리스트 인덱스 현재위치를 오른쪽으로 한칸 옮김

        else:    # 오른쪽이 작으면
            result[k]=right[j]
            j = j+1

        k = k+1   # result 의 인덱스 현재위치는 무조건 증가

    # while 문이 끝났는데, 왼쪽이나 오른쪽 리스트의 인덱스가 끝까지 가지 못했다면, 전부를 추가해줌

    if i < len(left):   # 왼쪽의 요소가 남아있으면
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

    # 1. divide
    if len(data) <= 1: # 항이 하나로 쪼개지면
        return data  # 쪼개진 애를 return 시킨다

    mid = len(data)//2
    left = data[:mid]  # 왼쪽 부분
    right = data[mid:]  # 오른쪽 부분

    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


print(merge_sort(data))

