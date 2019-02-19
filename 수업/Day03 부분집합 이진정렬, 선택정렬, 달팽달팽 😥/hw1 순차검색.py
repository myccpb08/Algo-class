def sequentialSearch(a, n, key):
    i=0
    while i<n and a[i]!=key:
        i+=1
    if i<n:
        return print(f'{i+1}번 시도로 {key} 찾았음')
    else:
        return print(f'{key}가 해당 범위에 없습니다')



sequentialSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 6)

sequentialSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11)