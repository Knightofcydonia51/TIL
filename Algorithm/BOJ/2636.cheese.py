import sys
sys.stdin=open('2636.cheese.txt')

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    visit[y][x]=1
    q=[]
    q.append((y,x))
    while q:
        y,x=q.pop(0)
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if -1<ny<N and -1<nx<M and visit[ny][nx]==0:
                if cheese[ny][nx]==1:
                    cheese[ny][nx]=100
                    visit[ny][nx]=1
                elif cheese[ny][nx]==0:
                    q.append((ny,nx))
                    visit[ny][nx]=1


N, M = map(int, input().split()) #세로, 가로
cheese=[[int(x) for x in input().split()]for y in range(N)]

# 0인 칸을 전부 탐색(1칸은 침범 할 수 있게 탐색)
# 침범된 모든 칸을 제거

cnt=0
while 1:
    cnt+=1
    visit = [[0 for x in range(M)] for y in range(N)]
    bfs(0,0)
    remains = 0
    empty=0
    for y in range(N):
        for x in range(M):
            if cheese[y][x]==100:
                cheese[y][x]=0
                remains+=1
            elif cheese[y][x]==0:
                empty+=1
    if remains+empty==N*M:
        break
print(cnt)
print(remains)

