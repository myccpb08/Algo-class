import sys
sys.stdin = open('hw6.txt', 'r')

def pal(word,length):
    for time in range(100-length+1):
        for j in range(length// 2):
            if word[time + j]!=word[time+length-j-1]:
                break
            if j==length//2-1:
                return length
for i in range(1,11):
    print('#'+input(),end=' ')
    word=[input() for j in range(100)]
    flag = 0
    for length in range(100, 0, -1):
        for i in word:
            if pal(i,length)!=None:
                a=pal(i,length)
                flag = 1
                break
        if flag==1:
            break
    word2 = []
    for i in range(100):
        v=''
        for j in range(100):
            v+=word[j][i]
        word2+=[v]
    flag = 0
    for length in range(100, 0, -1):
        for i in word2:
            if pal(i, length) != None:
                b=pal(i, length)
                flag = 1
                break
        if flag == 1:
            break
    print(max(a,b))
