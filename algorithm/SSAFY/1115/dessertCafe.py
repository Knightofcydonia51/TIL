
dy=[1,1,-1,-1]#우하,좌하,좌상,우상
dx=[1,-1,-1,1]

def dfs(y,x):
    visit[y][x]=1
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if N > y > -1 and N > x > -1:
            if sheet[ny][nx]



T=int(input())
for i in range(T):
    N=int(input())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    visit=[[0 for x in range(N)]for y in range(N)]

