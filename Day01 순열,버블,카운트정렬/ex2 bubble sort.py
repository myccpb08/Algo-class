def bubble(a):
    for i in range(len(a)-1):
        for j in range(0, len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(a)


bubble([3, 4, 2, 5, 1])
bubble([5, 4, 3, 2, 1])
