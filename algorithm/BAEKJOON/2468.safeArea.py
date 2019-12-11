import sys
sys.stdin=open('2468.safeArea.txt')

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    global check
    visit[y][x]=check
    q =[]
    q.append((y,x))
    while q:
        y,x=q.pop(0)
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if -1<ny<N and -1<nx<N:
                if visit[ny][nx] == 0 and sheet[ny][nx]>water:
                    visit[ny][nx]=check
                    q.append((ny,nx))


N=int(input())
sheet=[[int(x) for x in input().split()] for y in range(N)]


# 잠기게 할 변수 water을 1씩 늘리면서 water 보다 많은 애들만 dfs로 탐색
# 안전 영역들의 수를 체크
# max
# 가장 높은 수위까지만 실행

highest=0

for y in range(N):
    for x in range(N):
        if sheet[y][x]>highest:
            highest=sheet[y][x]

maxi=0

for water in range(1,highest):
    visit = [[0 for x in range(N)] for y in range(N)]
    check=0
    for y in range(N):
        for x in range(N):
            if visit[y][x]==0 and sheet[y][x]>water:
                check+=1
                bfs(y,x)
    if check>maxi:
        maxi=check
if maxi==0:
    maxi=1
print(maxi)


