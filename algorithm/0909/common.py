import sys
sys.stdin=open('common.txt')

def inorder(node):
    global anc
    if info[node][3] == 1:
        anc = node
        preorder(node)
    elif node!=0:
        info[node][3]=1
        inorder(info[node][2])

def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(info[node][0])
        preorder(info[node][1])
'''
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 11 6 10 11 13
'''
T=int(input())
for i in range(T):
    V,E,A,B=map(int,input().split())
    nodes=[int(x) for x in input().split()]
    info=[[0 for x in range(4)]for y in range(V+1)]
    for j in range(0, len(nodes) - 1, 2):
        if info[nodes[j]][0] == 0: # 왼쪽이 아직 입력되지 않았을 때.
            info[nodes[j]][0] = nodes[j + 1] #node j의 왼쪽에 대한 정보 입력
            info[nodes[j + 1]][2] = nodes[j] #node j의 왼쪽인 node j+1의 부모는 node j라는 표시. 부모에 대한 정보 입력.
        else:
            info[nodes[j]][1] = nodes[j + 1] #왼쪽이 입력이 끝난 후, 즉 오른쪽 입력할 차례
            info[nodes[j + 1]][2] = nodes[j] #부모 표시
    print(nodes)
    print(info)

    anc=0
    cnt=0
    inorder(A)
    inorder(B)
    print('#{} {} {}'.format(i+1,anc,cnt))
