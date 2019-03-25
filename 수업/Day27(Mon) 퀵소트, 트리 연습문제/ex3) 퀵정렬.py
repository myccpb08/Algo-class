arr = [30,45,23,81,28,34]
data_b = [11,45,22,81,23,34,99,22,17,8]
data_c = [1,1,1,1,1,0,0,0,0,0]

def partition(arr, left, right):
    if left>=right:
        return

    i,j = left, right
    pivot = arr[left]   # 시작점이 pivot

    while i<=j:
        while arr[i]<=pivot and i<=right:  # pivot 보다 큰 값을 만날 때까지 이동
            i = i+1
        while arr[j]>=pivot and j>=left:  # pivot 보다 작은 값을 만날 때까지 이동
            j = j-1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]  # i 와 j 자리 교환

    arr[left], arr[i] = arr[i], arr[left]  # i 와 피봇 자리 교환

    partition(arr, left, j-1)
    partition(arr,j+1, right)


partition(arr, 0, len(arr)-1)
# partition(data_b, 0, len(data_b)-1)
# partition(data_c, 0, len(data_c)-1)

print(arr)
# print(data_b)
# print(data_c)



