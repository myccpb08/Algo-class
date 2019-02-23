def paper(n):
    if n < 3:
        return 2*n-1
    else:
        return 2*paper(n-2) + paper(n-1)


for i in range(int(input())):
    n = int(input())//10

    print(f'#{i+1} {paper(n)}')

paper()