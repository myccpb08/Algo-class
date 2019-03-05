node = 13   # node가 13이니까, path는 12개
path = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

Left_Child = [0]*(node+1)
Right_Child = [0]*(node+1)
many_child = [0]*(node+1)
parent_who = [0]*(node+1)
level = [0]*(node+1)

for i in range(12):
    parent = path[2*i]
    child = path[2*i +1]

    parent_who[child] = parent  # 부모정보 입력
    level[child] = level[parent] + 1  # 레벨정보 입력

    many_child[parent] += 1  # 자식수정보 입력

    if Left_Child[parent]==0: # 왼쪽 자식이 없으면
        Left_Child[parent]=child  #왼쪽에 넣어라
    else:
        Right_Child[parent]=child    # 왼쪽 자식 있으면 오른쪽에 넣어라


# 전위순회
def preorder(root):
    if root:
        print('{}'.format(root), end=' ')
        preorder(Left_Child[root])
        preorder(Right_Child[root])

print("# 전위순회 : 루트-왼-오")
preorder(1)
print()
print()


# 중위순회
def inorder(t):
    if t:
        inorder(Left_Child[t])
        print('{}'.format(t), end=' ')
        inorder(Right_Child[t])

print("# 중위순회 : 왼-루트-오")
inorder(1)
print()
print()


# 후위순회
def postorder(t):
    if t:
        postorder(Left_Child[t])
        postorder(Right_Child[t])
        print('{}'.format(t), end=' ')

print("# 후위순회 : 왼-오-루트")
postorder(1)
print()
print()


# 레벨순회 . bfs?
levelq=[]
def levelroad(t):
        global levelq
        levelq.append(t)
        while levelq!=[]:
                start_node = levelq.pop(0)
                print(start_node, end=' ')
                if Left_Child[start_node] != 0:
                        levelq.append(Left_Child[start_node])
                if Right_Child[start_node] != 0:
                        levelq.append(Right_Child[start_node])
print("# 레벨순회 : 왼-오")
levelroad(1)
print()
print()




# 각 레벨
print('# 레벨')
for i in range(1,max(level)+1):
    print('lv{}'.format(i),end=' ')
    for j in range(1,14):
        if level[j]==i:
            print(j, end=' ')
    print()
print()


# 13의 부모들
print('#13의 부모들')
def par(de):
    print(parent_who[de],end=' ')
    if parent_who[de]==1:
        return
    par(parent_who[de])

par(13)
print()
print()


# 사촌


