import sys
sys.stdin = open('다이아몬드.txt', 'r')

for i in range(int(input())):
    a=input()
    b,c,d,e,f=len(a),'..#.','.#','.',''
    for j in a:
        f+='#.'+j+e
    g=[b*c+e,2*b*d+e,f+'#',2*b*d+e,b*c+e]
    print('\n'.join(g))