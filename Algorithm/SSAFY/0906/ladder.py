import sys
sys.stdin=open('ladder.txt')

dy=[0,0,1] #좌 우 하
dx=[-1,1,0]

def dfs(y,x):
    global step
    global flag
    if flag==1:
        return
    visited[y][x]=1
    for z in range(3):
        testy=y+dy[z]
        testx=x+dx[z]
        if -1<testx<N and -1<testy<N and visited[testy][testx]==0 and ladder[testy][testx]==1:
            step+=1
            dfs(testy,testx)
            if testy==99:
                flag=1

for i in range(10):
    n=input()
    ladder=[[int(x) for x in input().split()]for y in range(100)]
    N=len(ladder)
    mini=0xfffffff
    for j in range(1):
        for k in range(N):
            if ladder[j][k]==1:
                visited =[[0 for x in range(N)]for y in range(N)]
                step=0
                flag=0
                dfs(j,k)
                if step<=mini:
                    mini=step
                    maxx=k
    print('#{} {}'.format(i+1,maxx))

