import sys
sys.stdin=open('mountain.txt')

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def dfs(y,x,cnt):
    global longway
    if cnt>longway:
        longway=cnt
    visit[y][x]=1
    for i in range(4):
        ny=dy[i]+y
        nx=dx[i]+x
        if N>ny>-1 and N>nx>-1:
            if sheet[ny][nx]<sheet[y][x]:
                dfs(ny,nx,cnt+1)


T=int(input())

for i in range(T):
    N,K=map(int,input().split())
    sheet=[[int(x) for x in input().split()] for y in range(N)]
    visit=[[0 for x in range(N)] for y in range(N)]
    maxi=0
    longway=1
    for k in range(N):
        for j in range(N):
            if sheet[k][j]>maxi:
                maxi=sheet[k][j]
        # print(K,m)
    for k in range(N):
        for j in range(N):
            for m in range(K + 1):
                sheet[k][j]-=m
                for y in range(N):
                    for x in range(N):
                        if sheet[y][x]==maxi:
                            cnt=1
                            dfs(y,x,cnt)
                            visit = [[0 for x in range(N)] for y in range(N)]
                sheet[k][j]+=m
    print('#{} {}'.format(i+1,longway))

