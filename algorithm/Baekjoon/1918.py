import sys
sys.stdin=open('tomato.txt')

dy = [1, -1, 0, 0, 0, 0]  # 앞뒤좌우상하
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def one(y, x):
    global willripe
    visit[0][y][x] = 1
    q = []
    q.append((y, x))
    while q:
        q.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < ny < N and -1 < nx < M and visit[0][ny][nx] == 0 and box[0][ny][nx] == 0:
                q.append((ny, nx))
                visit[0][ny][nx] = 1
                ripelist.append([0,ny,nx])
                willripe += 1

def ripeBfs(z, y, x):
    global willripe
    visit[z][y][x] = 1
    q = []
    q.append((z, y, x))
    while q:
        q.pop(0)
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < nz < H and -1 < ny < N and -1 < nx < M and visit[nz][ny][nx] == 0 and box[nz][ny][nx] == 0:
                q.append((nz, ny, nx))
                visit[nz][ny][nx] = 1
                ripelist.append([nz,ny,nx])
                willripe+=1

# def bfs(z, y, x):
#     global flag
#     if flag>1:
#         return
#     visit[z][y][x] = 1
#     q = []
#     q.append((z, y, x))
#     while q:
#         z, y, x = q.pop(0)
#         for i in range(6):
#             nz = z + dz[i]
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if -1 < nz < H and -1 < ny < N and -1 < nx < M and visit[nz][ny][nx] == 0 and box[nz][ny][nx] != (-1):
#                 q.append((nz, ny, nx))
#                 visit[nz][ny][nx] = 1


M, N, H = map(int, input().split())

box = [[[int(x) for x in input().split()] for y in range(N)] for z in range(H)]
# 1 = 익은거   0 = 안익은거   -1 = 빈칸


# 모두 익은 상황 = 0이 하나도 없으면서 1인 칸과 -1인 칸의 합이 모든 칸의 합일때
# 모든 칸이 빈 경우, 익힐 토마토가 하나도 없는 경우
ans = (-1)
zeroCnt = 0
tomato = 0

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                zeroCnt += 1
            elif box[z][y][x] == 1:
                tomato += 1

if zeroCnt == 0:
    if tomato == 0:  # 모든 칸이 -1인 경우
        print(ans)
    else:  # 0인 애들이 하나도 없으면서 토마토는 있는 경우 : 모든 토마토가 익어있음
        print(0)

else:
    ans = 0
    while 1:
        ripelist = []
        ans += 1
        visit = [[[0 for x in range(M)] for y in range(N)] for z in range(H)]
        tomato = 0
        willripe=0
        empCnt=0
        for z in range(H):
            for y in range(N):
                for x in range(M):
                    if box[z][y][x] == 1:
                        tomato+=1
                        if H == 1:
                            one(y, x)
                        else:
                            ripeBfs(z, y, x)
                    elif box[z][y][x]==(-1):
                        empCnt+=1

        # 익힐 토마토와 익은 토마토의 합이 -1을 제외한 박스 내 칸의 총합과 같다면 종료
        if tomato+willripe==(N*M*H)-empCnt:
            print(ans)
            break
        elif willripe==0:
            print(-1)
            break
        while ripelist:
            z,y,x=ripelist.pop()
            box[z][y][x]=1

