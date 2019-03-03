numbers = list(map(int,input().split()))  # 정렬되어 있는 리스트
start = 0   # 인덱스의 시작
end = len(numbers)-1  # 인덱스의 끝
want_number_index = 0

def binary_recursion(start, end, want_number):
    global numbers
    global want_number

    if numbers[start]==want_number:
        want_number_index = start
        return
    elif numbers[end]==want_number:
        want_number_index = end
        return
    else:
        mid = (start + end)//2
        if mid == start:
            want_number = -1
            return
        else:
            if want_number > numbers[mid]:
                start = mid
            else:
                end = mid
    binary_recursion(start, end, want_number)

print(want_number_index)
