a='algorithm'

b=list(a)
length = len(b)

for i in range(length//2):
    b[i], b[length-1-i] = b[length-1-i], b[i]

print(''.join(b))