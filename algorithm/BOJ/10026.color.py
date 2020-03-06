import sys
sys.stdin=open('10026.color.txt')

import collections

def bfs(y,x,col): # 모든 구역 탐색용
    q=collections.deque([(y,x)])
    if col=='B':
        visited[y][x]=2
    else:
        visited[y][x]=1
    while q:
        y,x=q.popleft()
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
            ny=y+i[0]
            nx=x+i[1]
            if -1<ny<N and -1<nx<N and visited[ny][nx]==0 and sheet[ny][nx] == col:
                q.append((ny, nx))
                if col=='R' or col =='G':
                    visited[ny][nx]=1
                else:
                    visited[ny][nx]=2

def bfs2(y,x): # 색약용
    global blind
    q=collections.deque([(y,x)])
    visited[y][x]=3
    while q:
        y,x=q.popleft()
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
            ny=y+i[0]
            nx=x+i[1]
            if -1<ny<N and -1<nx<N and visited[ny][nx]==1:
                q.append((ny, nx))
                visited[ny][nx]=3




N=int(input())
sheet=[[x for x in input()]for y in range(N)]
visited=[[0 for x in range(N)]for y in range(N)]
rg=0
blind=0
blue=0

for y in range(N):
    for x in range(N):
        if visited[y][x]==0 and sheet[y][x]!='B':
            bfs(y,x,sheet[y][x])
            rg+=1
        elif visited[y][x]==0 and sheet[y][x]=='B':
            bfs(y, x, sheet[y][x])
            blue+=1

for y in range(N):
    for x in range(N):
        if visited[y][x]==1:
            bfs2(y,x)
            blind+=1


print(rg+blue,blind+blue)


