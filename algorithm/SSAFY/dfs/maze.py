import sys
sys.stdin=open("maze.txt")

def dfs(i, j):
    global a
    visited[i][j] = 1

    dx = [0, 0, -1, 1]  # 하 상 좌 우
    dy = [-1, 1, 0, 0]
    for z in range(4):
        nx = i + dx[z]
        ny = j + dy[z]
        if -1 < nx < 16 and -1 < ny < 16:
            if maze[nx][ny] != 1 and visited[nx][ny] == 0:
                dfs(nx, ny)
            if maze[nx][ny] ==3:
                a=0
                return a

for i in range(10):
    N=int(input())
    maze=[[int(x) for x in input()]for y in range(16)] # 지도
    # visited=[[0 for x in range(16)]for y in range(16)] # 포인터
    visited = [[0]*16 for _ in range(16)]
    # print(maze)

    a = 1
    for k in range(len(maze)):
        for j in range(len(maze)):
            if maze[k][j] == 2 and visited[k][j] == 0:
                dfs(k, j)
                if a==0:
                    print('#{} 1'.format(i+1))
                else:
                    print('#{} 0'.format(i+1))

    # for i in range(16):
    #     # print(data[i])
    #     print(N,visited[i])
