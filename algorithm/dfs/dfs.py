'''
7 8 노드수, 간선수
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 간선정보
'''
import sys
sys.stdin=open("dfs.txt")

def dfs(v):
    visited[v]=1 # visited[1]=1
    print(v,end=" ") # 1

    for w in range(V+1):
        if G[v][w]==1 and visited[w]==0:
            dfs(w)

V, E = map(int,input().split())

temp=list(map(int,input().split()))

G=[[0 for i in range(V+1)] for j in range(V+1)]
visited=[0 for i in range(V+1)]

print(temp)

for i in range(0,len(temp),2):
    G[temp[i]][temp[i+1]]=1 # 1,2
    G[temp[i+1]][temp[i]]=1 #2,1

for i in range(V+1):
    print("{} {}".format(i,G[i])) # 지도 출력

dfs(1)



