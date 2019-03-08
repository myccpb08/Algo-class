#combi=[]
#tmp=[0,0]
lst=[1,2,3,4]
visited = [0,0,0,0]

def combination(num,count,location):  # num : 몇 개 넣었는지   count: 원하는 공개수  # location : 현재 위치
    if num >= count:
        # combi.append
        for i in range(len(visited)):
            if visited[i]:
                print(lst[i],end=" ")
        print()
        return

    elif location >= len(lst):
        return

    else:
        # tmp[num] = lst[location]
        visited[location] = 1
        combination(num + 1, count, location + 1)
        # tmp[num] = 0
        visited[location] = 0
        combination(num,count,location+1)
combination(0,2,0)
# print(combi)