import sys
sys.stdin=open("05.maze.txt")

def dfs(k,j):
    global cnt
    visited[k][j]=1
    x=j
    y=k
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    for i in range(4):
        testx = x+dx[i]
        testy = y+dy[i]
        if N>testy>-1 and N>testx>-1:
            if map[testy][testx]==2:
                cnt+=1
            elif map[testy][testx]!=1 and map[testy][testx]!=3 and visited[testy][testx]==0:
                dfs(testy, testx)

T=int(input())


for i in range(T):
    N=int(input())
    map=[[int(x) for x in input()]for y in range(N)]
    visited=[[0 for x in range(N)]for y in range(N)]

    cnt=0
    for k in range(N):
        for j in range(N):
            if map[k][j]==3 and visited[k][j]==0:
                dfs(k,j)
    if cnt==1:
        print("#{} {}".format(i+1,cnt))
    else:
        print("#{} 0".format(i + 1))
