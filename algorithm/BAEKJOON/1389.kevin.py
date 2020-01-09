import sys
import collections
sys.stdin=open('1389.kevin.txt')


def bfs(v,obj):
    visit=[0 for x in range(N+1)]
    q=collections.deque([(v,0)])
    visit[v]=1
    dis=0
    while q:
        v,dis=q.popleft()
        dis += 1
        if v==obj:
            return dis
        for w in range(1,N+1):
            if G[v][w]==1 and visit[w]==0:
                visit[w]=1
                q.append((w,dis))





N,M = map(int, input().split())
info=[list(map(int,input().split())) for x in range(M)]
G=[[0 for x in range(N+1)]for y in range(N+1)]

mini=999999

for i in range(M):
    G[info[i][0]][info[i][1]]=1
    G[info[i][1]][info[i][0]]=1

kevin=0
flag=0
ans=0


for i in range(1,N+1):
    for k in range(1,N+1):
        if i!=k:
            kevin+=bfs(i,k)
    if kevin<mini:
        mini=kevin
        ans=i

print(i,kevin)




