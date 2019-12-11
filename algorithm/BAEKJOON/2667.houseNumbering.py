import sys
sys.stdin=open('2667.houseNumbering.txt')

dy=[-1,1,0,0]
dx=[0,0,-1,1]


def bfs(y,x):
    global step
    global check
    step=1
    visit[y][x]=step
    q=[]
    q.append((y,x))
    while q:
        y,x=q.pop(0)
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if -1<ny<N and -1<nx<N and visit[ny][nx]==0 and sheet[ny][nx]==1:
                step+=1
                q.append((ny,nx))
                visit[ny][nx]=step



N=int(input())

sheet=[[int(x) for x in input()]for y in range(N)]
visit=[[0 for x in range(N)]for y in range(N)]

check=0
ans=[]
for y in range(N):
    for x in range(N):
        if sheet[y][x]==1 and visit[y][x]==0:
            check+=1
            bfs(y,x)
            ans.append(step)
ans.sort()
print(check)
for i in range(len(ans)):
    print(ans[i])
