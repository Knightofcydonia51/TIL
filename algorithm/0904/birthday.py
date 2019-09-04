import sys
sys.stdin=open("birthday.txt")


def bfs(v):
    visited[v]=1
    queue=[]
    queue.append(v)
    while len(queue)!=0:
        v=queue.pop(0)
        for w in range(N+1):
            if G[v][w]==1 and visited[w]==0:
                queue.append(w)
                visited[w]=visited[v]+1
                if visited[w]>=4:
                    break

T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    visited=[0 for x in range(M+1)]
    G=[[0 for x in range(N+1)]for y in range(N+1)]

    for j in range(M):
        u, v = map(int, input().split())
        G[u][v] = G[v][u] = 1

    bfs(1)
    flag=0
    for k in range(len(visited)):
        if 1<visited[k]<4:
            flag+=1
    print('#{} {}'.format(i+1,flag))