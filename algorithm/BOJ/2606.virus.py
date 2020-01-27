import collections
import sys
sys.stdin=open('2606.virus.txt')

def bfs(v):
    ans=0
    visit=[0 for x in range(len(G))]
    visit[v]=1
    q=collections.deque([v])
    while q:
        v=q.popleft()
        for w in range(1,len(G)):
            if G[v][w]==1 and visit[w]==0:
                visit[w]=1
                q.appendleft(w)
                ans+=1
    return ans

N=int(input())
M=int(input())
nodes=[list(map(int,input().split())) for i in range(M)]
G=[[0 for i in range(N+1)] for y in range(N+1)]
start=0
for y in range(M):
    if nodes[y][0]==1:
        if not start:
            start=y
    G[nodes[y][0]][nodes[y][1]]=1
    G[nodes[y][1]][nodes[y][0]]=1

print(bfs(nodes[start][0]))
# for y in range(len(G)):
#     print(y,G[y])