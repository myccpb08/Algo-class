for case in range(int(input())):
    n,m = map(int,input().split())  # n=숫자 개수, m=옮긴 횟수
    numbers = list(map(int,input().split()))
    answer = m%n
    print(f'#{case+1} {numbers[answer]}')