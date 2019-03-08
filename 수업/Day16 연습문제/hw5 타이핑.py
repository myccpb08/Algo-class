for i in range(int(input())):
        a,b=input().split()
        print('#{} {}'.format(i+1,a.count(b)+len(a.replace(b, ""))))
