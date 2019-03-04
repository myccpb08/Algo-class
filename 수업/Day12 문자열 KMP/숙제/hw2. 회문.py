import sys
sys.stdin = open('hw2.txt', 'r')

for tc in range(int(input())):
    size, length = map(int,input().split())
    quiz = [input() for i in range(size)]

    # 가로
    def palindrome(size, length, word):
        for time in range(size - length + 1):
            if word[time]==word[time+length-1]:  # 첫 글자와 끝 글자가 같으면
                for j in range(length//2):
                    if word[time+j]!=word[time+length-1-j]:
                        break
                    if j == length // 2 - 1:
                        return word[time:time + length]



    for word in quiz:
        if palindrome(size, length, word) != None:
            print("#{} {}".format(tc+1, palindrome(size, length, word)))
            break



    #세로

    quiz2 = []
    for i in range(size):    # 열
        vertical = ''
        for j in range(size):  # 행
            vertical += quiz[j][i]
        quiz2.append(vertical)


    for vertical in quiz2:
        if palindrome(size, length, vertical) != None:
            print("#{} {}".format(tc+1, palindrome(size, length, vertical)))
            break







