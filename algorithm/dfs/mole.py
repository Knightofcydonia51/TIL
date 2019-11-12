def dfs(i,j):
   global a
   visited[i][j] = a

   global cnt
   cnt += 1
   dx = [0,0,-1,1] #하 상 좌 우
   dy = [-1,1,0,0]
   for z in range(4):
       nx = i + dx[z]
       ny = j + dy[z]
       if -1 < nx < 7  and -1 < ny < 7:
           if data[nx][ny]== 1 and visited[nx][ny]==0:
               dfs(nx,ny)

import sys
sys.stdin = open("mole.txt")
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

b=[]
a = 1
for i in range(len(data)):
   for j in range(len(data)):
       cnt = 0
       if data[i][j]==1 and visited[i][j]==0:
           dfs(i,j)
           b.append(cnt)
           a+=1
for i in range(N):
   # print(data[i])
   print(visited[i])
for i in range(len(b)):
   print(b[-(i+1)])
print(a, b)