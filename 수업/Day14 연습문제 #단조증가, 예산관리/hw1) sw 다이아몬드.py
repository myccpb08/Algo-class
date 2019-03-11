import sys
sys.stdin = open('다이아몬드.txt', 'r')

for i in range(int(input())):
    a=input()
    b=len(a)
    print('..#.'*b+'.')
    print('.#'*2*b+'.')
    for j in a:
        print('#.'+j+'.',end='')
    print('#')
    print('.#' * 2 * b + '.')
    print('..#.' * b + '.')

