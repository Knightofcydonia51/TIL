import sys
sys.stdin=open('subtree.txt')

def preorder(node):
    global cnt
    if node!=0:
        cnt+=1
        preorder(info[node][0])
        preorder(info[node][1])


T=int(input())

for i in range(T):
    E,N=map(int,input().split())
    nodes=[int(x) for x in input().split()]
    info=[[0 for x in range(3)]for y in range(E+2)]
    for j in range(0,len(nodes)-1,2):
        if info[nodes[j]][0]==0:
            info[nodes[j]][0]=nodes[j+1]
            info[nodes[j+1]][2]=nodes[j]
        else:
            info[nodes[j]][1]=nodes[j+1]
            info[nodes[j + 1]][2] = nodes[j]
    cnt=0
    preorder(N)
    print('#{} {}'.format(i+1, cnt))