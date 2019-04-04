import sys
sys.stdin=open('정사각형.txt','r')

def money(x,chance,sample):  # x: 현재 탐색위치, chance: 시도횟수, sample: 현재 완성된 값
    global mymin
    if chance == tries:
        #sample = int(''.join(list(map(str,sample))))
        result = 0
        for i in range(len(sample)):
            result = result*10 + sample[i]
        if result > mymin:
            mymin=result

    else:
        now = sample[x]  # 바꾸고 싶은 값
        cand = sample[x+1:]  # now 보다 뒤에 꺼
        temp = 




for t in range(int(input())):
    num,tries = map(int,input().split())
    num = list(map(int,str(num)))
    mymin = -1
    money(0,0,num)  #

    print('#{} {}'.format(t+1,mymin))