# def dfs(v):
#     visited[v]=1 # visited[1]=1
#     print(v,end=" ") # 1
#
#     for w in range(V+1):
#         if G[v][w]==1 and visited[w]==0:
#             dfs(w)

import sys
sys.stdin=open("ladder.txt")

for i in range(10):
    N=input()
    ladder=[[int(x) for x in input().split()] for y in range(100)]
    startpoint=0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for j in range(100):
        if ladder[100][j]==2:
            startpoint=j
            break

    dx = [-1, 1,0]
    dy = [0,0,1]

    for y in range(len(ladder)):
        for x in range(len(ladder)-1,-1,-1):
            for i in range(3):
                testY = y + dx[i]
                testX = x + dx[i]
                if ladder[testY][testX]:

# def whereigo(x, y):
#     if 0 <= y + dy[0] and y + dy[0] <= 99 and 0 <= x + dx[0] and x + dx[0] <= 99:
#         if ladder[y + dy[0]][x + dx[0]] == 1:
#             return 0
#     if 0 <= y + dy[1] and y + dy[1] <= 99 and 0 <= x + dx[1] and x + dx[1] <= 99:
#         if ladder[y + dy[1]][x + dx[1]] == 1:
#             return 1
#     if ladder[y + dy[2]][x + dx[2]] == 1:
#         return 2
#
#
# T = 10
# for tc in range(T):
#     r_tc = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#     x = ladder[99].index(2)
#     y = 99
#
#     dx = [1, -1, 0]  # 우 좌 상
#     dy = [0, 0, -1]
#
#     while y >= 0:
#         k = whereigo(x, y)
#         ladder[y][x] = 5
#         x = x + dx[k]
#         y = y + dy[k]
#
#     print('#{} {}'.format(r_tc, x))