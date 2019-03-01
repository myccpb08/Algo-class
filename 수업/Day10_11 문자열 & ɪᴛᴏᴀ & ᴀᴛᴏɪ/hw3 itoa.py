i = 1234

# 몇 번 반복할지  미리 정하기
n=0
while True:
    if i < 10**n:
        break
    n += 1   # n=4

change = ''
count =0
while count!=n:
    number = i % 10
    change = chr(ord('0') + number) + change
    i = (i - number)//10
    count  += 1

print(change)
print(type(change))