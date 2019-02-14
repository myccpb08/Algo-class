a = list(map(int, input().split()))
counts = [0] * (max(a) + 1)

for i in a:
    counts[i] += 1

run = triplet = 0

for i in range(len(counts)):
    if counts[i]//3 >=1 :
        triplet += counts[i]//3
        counts[i] -= (counts[i]//3 * 3)

for j in range(len(counts)-2):
    if counts[j] == counts[j+1] == counts[j+2] == 1:
        run += 1
        break
    elif counts[j] == counts[j+1] == counts[j+2] == 2:
        run += 2
        break

if run + triplet == 2:
    print('Baby Jin 입니다')
else:
    print('아닙니다')