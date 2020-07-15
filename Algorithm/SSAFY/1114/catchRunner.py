import sys
sys.stdin=open('catchRunner.txt')

dy=[-1,1,0,0]
dx=[0,0,-1,1]



def bfs(y,x):
    visit[y][x]=1
    q=[]
    q.append((y,x,visit[y][x]))
    while q:
        y,x,z=q.pop(0)
        if z==L:
            break
        if sheet[y][x]==1:
            start=0
            end=4
            step=1
        elif sheet[y][x]==2:
            start=0
            end=2
            step = 1
        elif sheet[y][x]==3: #좌, 우
            start=2
            end=4
            step = 1
        elif sheet[y][x]==4: # 상,우
            start=0
            end=4
            step = 3
        elif sheet[y][x]==5: # 하,우
            start=1
            end=4
            step = 2
        elif sheet[y][x]==6:
            start=1
            end=3
            step = 1
        else:
            start = 0
            end = 3
            step = 2
        for i in range(start,end,step):
            ny=y+dy[i]
            nx=x+dx[i]
            if N>ny>-1 and M>nx>-1:
                if visit[ny][nx]==0 and sheet[ny][nx]>0:
                    if sheet[ny][nx] == 1: #새 파이프가 상하좌우일때
                        visit[ny][nx] = visit[y][x] + 1
                        q.append((ny, nx, visit[ny][nx]))
                    else:
                        if sheet[y][x] == 1:
                            if i==0:
                                if sheet[ny][nx]==2 or sheet[ny][nx]==5 or sheet[ny][nx]==6:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i==1: # 2 4 7
                                if sheet[ny][nx]==2 or sheet[ny][nx]==4 or sheet[ny][nx]==7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i==2: # 3 4 5
                                if sheet[ny][nx]==3 or sheet[ny][nx]==4 or sheet[ny][nx]==5:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            else:
                                if sheet[ny][nx]==3 or sheet[ny][nx]==6 or sheet[ny][nx]==7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                        elif sheet[y][x]==2:
                            if i == 0:
                                if sheet[ny][nx] == 2 or sheet[ny][nx] == 5 or sheet[ny][nx] == 6:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i == 1:  # 2 4 7 아래로갈때
                                if sheet[ny][nx] == 2 or sheet[ny][nx] == 4 or sheet[ny][nx] == 7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                        elif sheet[y][x] == 3:
                            if i == 2:
                                if sheet[ny][nx] == 3 or sheet[ny][nx] == 4 or sheet[ny][nx] == 5:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i ==3:
                                if sheet[ny][nx] == 3 or sheet[ny][nx] == 6 or sheet[ny][nx] == 7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                        elif sheet[y][x] == 4:
                            if i == 0:
                                if sheet[ny][nx] == 2 or sheet[ny][nx] == 5 or sheet[ny][nx] == 6:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i==3: # 3 6 7 우측으로갈때
                                if sheet[ny][nx] == 3 or sheet[ny][nx] == 6 or sheet[ny][nx] == 7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                        elif sheet[y][x] == 5:
                            if i == 1:
                                if sheet[ny][nx] == 2 or sheet[ny][nx] == 4 or sheet[ny][nx] == 7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i == 3: # 3 6 7 우측으로갈때
                                if sheet[ny][nx] == 3 or sheet[ny][nx] == 6 or sheet[ny][nx] == 7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                        elif sheet[y][x] == 6:
                            if i == 1:
                                if sheet[ny][nx] == 2 or sheet[ny][nx] == 4 or sheet[ny][nx] == 7:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i == 2:  # 3 4 5
                                if sheet[ny][nx] == 3 or sheet[ny][nx] == 4 or sheet[ny][nx] == 5:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                        elif sheet[y][x]==7:
                            if i == 0:
                                if sheet[ny][nx] == 2 or sheet[ny][nx] == 5 or sheet[ny][nx] == 6:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))
                            elif i == 2:  # 3 4 5
                                if sheet[ny][nx]==3 or sheet[ny][nx]==4 or sheet[ny][nx]==5:
                                    visit[ny][nx] = visit[y][x] + 1
                                    q.append((ny, nx, visit[ny][nx]))

T= int(input())
for i in range(T):
    N,M,R,C,L=map(int,input().split())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    visit=[[0 for x in range(M)]for y in range(N)]
    bfs(R,C)
    ans=0
    for j in range(N):
        for k in range(M):
            if visit[j][k]>0:
                ans+=1
    print('#{} {}'.format(i+1,ans))
    #탐색 - 뎁스가 주어진 시간과 같으면, 브레이크
    # 그때까지 찍힌 visit의 개수를 확인하면 답이 나오지 않을까?



