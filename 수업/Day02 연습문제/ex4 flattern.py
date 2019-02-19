import sys
sys.stdin = open('ex4 flattern input.txt', 'r')


for i in range(10):
    tries = int(input())
    boxes = list(map(int, input().split()))
    for j in range(tries):
        max_location = boxes.index(max(boxes))
        min_location = boxes.index(min(boxes))
        boxes[max_location] -= 1
        boxes[min_location] += 1
    answer = max(boxes)-min(boxes)
    print(f'#{i+1} {answer}')