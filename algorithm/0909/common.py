import sys
sys.stdin=open('common.txt')

def dfs(w):
    global flag
    global common
    if flag==1:
        return
    visited[w] = 1
    for i in range(V+1):
        if visited[i]==0 and G[w][i]==1:
            dfs(i)
        elif visited[i]==1 and G[w][i]==1:
            flag+=1
            common=i
            return

def bfs(v):
    global cnt
    queue=[]
    queue.append(v)
    while len(queue)!=0:
        v=queue.pop(0)
        for w in range(V+1):
            if G[v][w]==2:
                cnt+=1
                queue.append(w)

'''
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 11 6 10 11 13
'''
T=int(input())
for i in range(T):
    V,E,A,B=map(int,input().split())
    nodes=[int(x) for x in input().split()]
    G=[[0 for x in range(V+1)]for y in range(V+1)]
    visited = [0 for x in range(V + 1)]

    for j in range(0, len(nodes), 2):
        G[nodes[j]][nodes[j + 1]] = 2
        G[nodes[j+1]][nodes[j]] = 1

    common=0
    flag=0
    dfs(A)
    dfs(B)

    cnt = 0
    bfs(common)

    print('#{} {} {}'.format(i+1,common,cnt+1))