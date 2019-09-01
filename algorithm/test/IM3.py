import sys
sys.stdin = open('IM3.txt', 'r')



T=int(input())
dx=[-1,-1,0,1,1,1,0,-1] #좌부터 시계방향
dy=[0,-1,-1,-1,0,1,1,1]

def dfs(j,k):
    global cnt
    y=j
    x=k
    visited[y][x]=1
    for u in range(8):
        testy=y+dy[u]
        testx = x + dx[u]
        if 0<testx<N and 0<testy<N and visited[testy][testx]==0 and islands[testy][testx]!=0:
            dfs(testy,testx)

for i in range(T):
    N=int(input())
    islands=[[int(x) for x in input().split()]for y in range(N)]
    visited=[[0 for x in range(N)]for y in range(N)]

    cnt=0
    for y in range(len(islands)):
        for x in range(len(islands)):
            if islands[y][x]!=0 and visited[y][x]==0:
                dfs(y,x)
                cnt += 1
    print('#{} {}'.format(i+1,cnt))