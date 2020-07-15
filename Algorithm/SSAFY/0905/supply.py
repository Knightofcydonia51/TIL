import sys
sys.stdin=open('supply.txt')

dy=[1,-1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):

    queue = []
    visited[y][x]=1
    queue.append(y)
    queue.append(x)
    while len(queue)!=0:
        tempy=queue.pop(y)
        tempx=queue.pop(x)
        for j in range(4):
            testy=tempy+dy[j]
            testx=tempx+dx[j]
            if -1<testy<N and -1<testx<N and visited[testy][testx]==0:
                visited[testy][testx]=1


T=int(input())

for i in range(T):
    N=int(input())
    sheet=[[int(x) for x in input()]for y in range(N)]
    dist=[[987654321]*N for _ in range(N)]
    visited=[[0 for x in range(N)]for y in range(N)]
    y=0;x=0
    bfs(0,0)