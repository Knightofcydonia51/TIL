import sys
sys.stdin=open("workOrder.txt")

def dfs(x, y):
    global a
    visited[y][x]=a

    dx=[-1,1,0,0,-1,1,-1,1] #좌우상하
    dy=[0,0,-1,1,-1,-1,1,1]
    for j in range(8):
        nx=x+dx[j]
        ny=y+dy[j]
        if 0< nx <V+1 and 0< ny <V+1:
            if G[ny][nx]>0 and visited[ny][nx]==0:
                dfs(nx,ny)

for i in range(1):
    V, E= map(int,input().split())
    temp=list(map(int,input().split())) # 1 4 1 3 2 3 2 5 4 6
    print(type(V))


    G = [[0 for i in range(V + 1)] for j in range(V + 1)] #노드수 +1을 지도로 받음.
    visited = [0 for i in range(V + 1)]

    for k in range(0, len(temp), 2):
        G[temp[k+1]][temp[k]] = 1  # 거꾸로 입력받음.
        # 룰 : 거꾸로 입력받으면 뿌리를 알 수 있음.
        # 후위에 2번이상 위치해있는 놈은 제거
        # 그다음 for문으로 다 돌려서, 제일 뒤에 위치해 있는 애들을 전부 리스트에 담음.
        # 중복을 제거하면 뿌리만 남는다?

    for y in range(len(G)):
        for x in range(len(G)):
            if G[y][x]==1 and visited[y][x] == 0:
                dfs(y, x)





