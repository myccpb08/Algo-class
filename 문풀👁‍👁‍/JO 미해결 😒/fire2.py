import sys
sys.stdin = open('fire.txt','r')

pump, car = map(int,input().split())

pumps = list(map(int,input().split()))
cars = list(map(int,input().split()))

total = sorted(pumps + cars)


a=[[]for i in range(2*pump)]

k=pump


def odd(data):
    aa=len(data)
    del data[aa//2]
    odd_sum = 0
    for i in range(0,aa-1,2):
        odd_sum += data[i+1]-data[i]
    return odd_sum


for what in total:
    if what in pumps:
        a[k]+=[what]
        k-=1
    else:
        k+=1
        a[k] += [what]

even_sum=0
oddd=0
for part in a:
    if len(part)!=0 and len(part)%2==0:
        for i in range(0,len(part),2):
            even_sum += part[i+1]-part[i]

    elif len(part)>=3:
        oddd += odd(part)
print(even_sum+oddd)