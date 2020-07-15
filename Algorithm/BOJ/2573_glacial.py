# 202 204 105 203

# 녹을 빙하 구하기 (while, dfs)
# k 한번 돌고 나서 다른 for문으로 빙하 지우기
# dfs돌려서 덩어리 계산하기
# 2덩이가 아니라면 계속 가고, 2덩이면 year 대입하고 break
# while이 끝났다면 0 대입하고 계산 종료


import sys
sys.stdin=open('2573_glacial.txt')


dy=[-1,1,0,0]
dx=[0,0,-1,1]

def delta(y,x):
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if glacial[ny][nx]==0:
            glacial[y][x]+=100

# def dfs(y,x,cnt):
#     if cnt>=2:
#         return
#     visit[y][x]=cnt
#     for i in range(4):
#         ny = dy[i] + y
#         nx = dx[i] + x
#         if glacial[ny][nx]>0 and visit[ny][nx]==0:
#             dfs(ny,nx,cnt)

def bfs(y,x,cnt):
    if cnt>2:
        return
    q=[]
    visit[y][x] = cnt
    q.append((y,x))
    while q:
        y,x=q.pop(0)
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if glacial[ny][nx]>0 and visit[ny][nx]==0:
                visit[ny][nx]=cnt
                q.append((ny,nx))

N,M=map(int,input().split())
glacial=[[int(x) for x in input().split()]for y in range(N)]
year=0

while True:
    visit=[[0 for x in range(M)]for y in range(N)]

    for y in range(1,N-1):
        for x in range(1,M-1):
            if glacial[y][x]>0:
                delta(y,x)

    for y in range(1,N-1):
        for x in range(1,M-1):
            if glacial[y][x]>100:
                share=(glacial[y][x] // 100)
                glacial[y][x]=glacial[y][x]-(share+(share*100))
                if glacial[y][x]<0:
                    glacial[y][x]=0

    cnt = 1
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if glacial[y][x] > 0 and visit[y][x] == 0:
                bfs(y, x, cnt)
                cnt += 1

    year += 1
    if cnt > 2:
        break

    if cnt == 1:
        year = 0
        break

print(year)

# 만약 cnt가 2번이상 증가했다면, 분리된 것이므로 break
#

