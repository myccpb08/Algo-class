data = [30,45,23,81,28,34]
data_b = [11,45,22,81,23,34,99,22,17,8]
data_c = [1,1,1,1,1,0,0,0,0,0]
data_d = [3,2,4,6,9,1,8,7,5]

def Quicksort(A,l,r): #A는 배열, l=lefth,r=right   시작과 끝
    if l < r:
        q = Partition(A,l,r)
        Quicksort(A,l,q)
        Quicksort(A,q+1,r)

def Partition(A,left,right):  # A는 배열,, right = len(A)
    pivot = A[left]
    i = left
    for j in range(left+1,right):
        if A[j] <= pivot:   # pivot 보다 큰 애를 찾아야함  / pivot 보다 크면 j 만 올라감
            i = i+1  # 데이터가 pivot 보다 작으면, i 랑 j 랑 같이 이동
            A[i],A[j] = A[j],A[i]

    A[left],A[i] = A[i], A[left]
    return i



# Quicksort(data,0,len(data))
# print(data)
# Quicksort(data_b,0,len(data_b))
# print(data_b)
# Quicksort(data_c,0,len(data_c))
# print(data_c)
Quicksort(data_d,0,len(data_d))
print(data_d)