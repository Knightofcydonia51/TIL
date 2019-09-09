def preorder(node):
    if node!=0:
        print("{}".format(node), end=" ")
        preorder(status[node][0])
        preorder(status[node][1])

def inorder(node):
    if node!=0:
        inorder(status[node][0])
        print("{}".format(node),end=" ")
        inorder(status[node][1])

def postorder(node):
    inorder(status[node][0])
    inorder(status[node][1])
    print("{}".format(node), end=" ")

def printTree():
    for i in range(1,N+1):
        print("%2d %2d %2d %2d" % (i, status[i][0],status[i][1], status[i][2]))


'''
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
N=13
V=[int(x) for x in input().split()]
G=[[0 for x in range(N+1)] for y in range(N+1)]
status=[[0 for x in range(3)]for y in range(N+1)]

for j in range(0,len(V),2):
    G[V[j]][V[j+1]]=1

for k in range(len(G)):
    print(G[k])

for y in range(1,len(status)):
    cnt=0
    for x in range(len(G)):
        if G[y][x]==1:
            status[y][cnt]=x
            status[x][2]=y #left, right,
            cnt+=1

printTree()

print(status)
preorder(1)
print()
inorder(1)
print()
postorder(1)
