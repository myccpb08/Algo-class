def binarySearch(a, key):
    a.sort()
    start = 0
    end = len(a)-1
    count = 0

    while start <= end:
        middle = (start+end) >> 1
        count += 1
        if a[middle] == key:  # 찾고자 하는 값 = 중간값이면, 바로 결과 반환
            return print(f'{count}번 시도로 {a[middle]} 찾았음')

        elif a[middle] > key:  # 찾고자 하는 값이 중간값보다 작으면, end 값을 계산한 중간 값으로 바꿈
            end = middle-1

        else:
            start = middle+1  # 찾고자 하는 값이 중간값보다 크면, start 지점을 중간값으로 바꿈



    return print('실패')



binarySearch([1,2,3,4,5,6,7,8,9,10], 11)