def next_permutation(a):

    num = list(a)
    can = 0
    for i in range(-1, -1*len(num),-1):
        if int(num[i]) > int(num[i-1]):
            can = i-1    # 2의 인덱스 찾음
            break

    if can == 0:
        return print(a)

    for j in range(-1, can, -1):
        if num[can] < num[j]:
            cand = j    # 2와 자리 바꿀 4의 인덱스를 찾음
            break

    num[can], num[cand] = num[cand], num[can]

    num = num[-1*(len(num)): can+1] + num[:can:-1]
    print(''.join(num))

next_permutation('54321')
next_permutation('32541')