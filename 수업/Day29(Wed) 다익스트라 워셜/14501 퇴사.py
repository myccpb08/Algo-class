import sys
sys.stdin = open('퇴사.txt', 'r')

n = int(input())
info = []

for i in range(n):
    t, p = map(int,input().split())
    info += [(t,p)]
print(info)

def sangdam():
    if

