m,n=map(int,input().split())
p=[1]*(n+1)
for i in range(2,n+1):
    if p[i]==1:
        if i<m:
            p[2*i::i]=[0]*((n//i)-1)
        else:
            print(i)
            p[2*i::i]=[0]*((n//i)-1)