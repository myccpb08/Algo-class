import sys
sys.stdin = open('바이러스.txt', 'r')

computer = int(input())
network = int(input())

mymap = [[0]*computer for i in range(computer)]

for i in range(network):
    a,b = map(int,input().split())
    mymap[a-1][b-1]=1
    mymap[b-1][a-1]=1

for trans in range(computer):
    for start in range(computer):
        for end in range(computer):
            mymap[start][end] = mymap[start][end] or (mymap[start][trans] and mymap[trans][end])

count = -1
for i in range(computer):
    if mymap[0][i]:
        count +=1

print(count)