def selectionSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    print(a)


selectionSort([9, 8, 7, 6, 5, 4, 3, 2, 1])