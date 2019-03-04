import sys
sys.stdin = open('hw1.txt', 'r')

for tc in range(int(input())):
    str1 = str(set(input()))
    str2 = input()

    my_dict={}

    for i in str1:
        for j in range(len(str2)):
            if str2[j]==i:
                if i in my_dict:
                    my_dict[i] += 1
                else:
                    my_dict[i] = 1

    print('#{} {}'.format(tc+1, max(my_dict.values())))