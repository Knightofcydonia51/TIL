import sys
sys.stdin=open("graphRoute.txt")

def dfs(v):
    visited[v]=1 # visited[1]=1
    # print(v,end=" ") # 1

    for w in range(V+1):
        if G[v][w]==1 and visited[w]==0:
            dfs(w)

T=int(input())
for i in range(T):
    V, E= map(int,input().split())
    temp=''
    for j in range(E):
        M=input()+' ' # 간선정보
        temp+=M
    temp=list(map(int,temp.split())) # 1 4 1 3 2 3 2 5 4 6
    # print(temp)
    print(V, E)

    G = [[0 for i in range(V + 1)] for j in range(V + 1)] #노드수 +1을 지도로 받음.
    visited = [0 for i in range(V + 1)]

    S,J= map(int,input().split()) #시작노드, 목표노드

    for k in range(0, len(temp), 2):
        G[temp[k]][temp[k + 1]] = 1  # 1 4


    # for i in range(V + 1):
    #     print("{} {}".format(i, G[i]))

    dfs(S)
    # print(visited)

    if visited[J]==1:
        print('#{} {}'.format(i+1,1))
    else:
        print('#{} {}'.format(i + 1,0))