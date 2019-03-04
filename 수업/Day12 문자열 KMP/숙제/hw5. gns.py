import sys
sys.stdin = open('hw5.txt', 'r')

for i in range(int(input())):
    input().split()
    c=input().split()
    l=["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
    print('#'+str((i+1)))
    [print((j+' ')*(c.count(j)),end=' ') for j in l]
    print()