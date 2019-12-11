import sys
import collections
sys.stdin=open('7569.tomato.txt')


dy = [1, -1, 0, 0]  # 앞뒤좌우상하
dx = [0, 0, -1, 1]


def one(y,x):
    visit[0][y][x] = 1
    q = collections.deque([])
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if -1 < ny < N and -1 < nx < M and visit[0][ny][nx] == 0 and box[0][ny][nx] == 0:
            visit[0][ny][nx] = 1
            willripe.append([0, ny, nx])


def ripeBfs(z, y, x):
    visit[z][y][x] = 1
    q = collections.deque([])
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if -1 < ny < N and -1 < nx < M and visit[z][ny][nx] == 0 and box[z][ny][nx] == 0:
            visit[z][ny][nx] = 1
            willripe.append([z,ny,nx])
        if z == 0:
            if box[1][y][x] == 0 and visit[1][y][x] == 0:
                visit[1][y][x] = 1
                willripe.append([1, y, x])
        elif z == H - 1:
            if box[z-1][y][x] == 0 and visit[z-1][y][x] == 0:
                visit[z-1][y][x] = 1
                willripe.append([z-1, y, x])
        else:
            if box[z-1][y][x] == 0 and visit[z-1][y][x] == 0:
                visit[z-1][y][x] = 1
                willripe.append([z-1, y, x])
            if box[z+1][y][x] == 0 and visit[z+1][y][x] == 0:
                visit[z+1][y][x] = 1
                willripe.append([z+1, y, x])


M, N, H = map(int, input().split())

box = [[[int(x) for x in input().split()] for y in range(N)] for z in range(H)]
visit = [[[0 for x in range(M)] for y in range(N)] for z in range(H)]
# 1 = 익은거   0 = 안익은거   -1 = 빈칸

# 모두 익은 상황 = 0이 하나도 없으면서 1인 칸과 -1인 칸의 합이 모든 칸의 합일때
# 모든 칸이 빈 경우, 익힐 토마토가 하나도 없는 경우
ans = (-1)
zeroCnt = 0
tomato = 0
ripelist = collections.deque([])

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                zeroCnt += 1
            elif box[z][y][x] == 1:
                tomato += 1
                ripelist.append([z,y,x])

if zeroCnt:
    ans = 0
    while zeroCnt:
        willripe = collections.deque([])
        ans += 1

        while ripelist:
            z,y,x=ripelist.popleft()
            if H==1:
                one(y,x)
            else:
                ripeBfs(z, y, x)

        while willripe:
            z,y,x=willripe.popleft()
            ripelist.append([z,y,x])
            box[z][y][x]=1
            zeroCnt-=1

        if len(ripelist) == 0:
            if zeroCnt:
                ans = - 1
                break
            else:
                break
    print(ans)


elif zeroCnt == 0:
    if tomato == 0:  # 모든 칸이 -1인 경우
        print(ans)
    else:  # 0인 애들이 하나도 없으면서 토마토는 있는 경우 : 모든 토마토가 익어있음
        print(0)


        # 익힐 토마토와 익은 토마토의 합이 -1을 제외한 박스 내 칸의 총합과 같다면 종료






