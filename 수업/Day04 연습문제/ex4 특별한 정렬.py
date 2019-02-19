import sys
sys.stdin = open('ex4.txt', 'r')

# bubble sort 로 입력받은 리스트 정렬
def bubble(a):
    for i in range(len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


for t in range(int(input())):  # 테스트 케이스 수
    n = int(input())  # 입력받을 수
    numbers = list(map(int, input().split()))  # 숫자리스트

    bubble(numbers)   # 입력받은 numbers 를 bubble 함수에 넣어서 정렬 시킴

    print(f'#{t+1}', end=' ')   # 케이스 번호 출력

    for i in range(5):     # 숫자 10개 출력이므로 절반인 5번 출력 반복
        print(numbers[-1*(i+1)], numbers[i], end=' ')  # (-1 → 0 → -2 → 1 → -3 → 2 → -4  →3 → -5 → 4 순서로 인덱스)

    print()




