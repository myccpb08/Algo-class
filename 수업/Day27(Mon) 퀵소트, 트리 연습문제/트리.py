import sys
sys.stdin = open('tree.txt')

def divide(post, mid):
    global result
    root = post[-1]
    result += str(root)

    pivot = mid.index(root)
    tree_size = pivot

    left_post = post[:pivot]
    right_post = post[pivot:2*pivot]
    left_in = mid[:pivot]
    right_in = mid[pivot:2*pivot]








n = int(input())
in_order = list(map(int,input().split()))  # 4 2 5   1     6 3 7
post_order = list(map(int,input().split()))  # 4 5 2   6 7 3 1
result = ''
level=1
while 2**level-1<n:
    level+=1

data = [0]*(2**level)

root = post_order[-1]   # root = 1
data[1]=root
data[2**(level-1)]=in_order[0]

pivot = in_order.index(root)
left_size = pivot

print(pivot)
print(data)

left_part = post_order[:pivot]