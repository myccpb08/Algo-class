import sys
sys.stdin = open('tree.txt')
sys.setrecursionlimit(100000000)

def divide(post, mid):
    global result
    root = post[-1]
    print(root, end=' ')

    if len(post)==1:
        return

    pivot = mid.index(root)
    left_post = post[:pivot]
    right_post = post[pivot:2*pivot]
    left_in = mid[:pivot]
    right_in = mid[pivot+1:2*pivot]

    divide(left_post, left_in)
    divide(right_post,right_in)

n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))

divide(post_order, in_order)