import sys
sys.stdin=open('1937.greedyPanda.txt')

from collections import deque

def val(y,x,z):
    global maxi
    for i in [1,0],[-1,0],[0,-1],[0,1]:
        ny=y+i[0]
        nx=x+i[1]
        if -1<ny<n and -1<nx<n and z<sheet[ny][nx]:
            if visited[ny][nx]<visited[y][x]+1:
                visited[ny][nx]=visited[y][x]+1
            if maxi<visited[ny][nx]:
                maxi=visited[ny][nx]


n=int(input())
sheet=[[int(x) for x in input().split()]for y in range(n)]
visited=[[1 for x in range(n)]for y in range(n)]
allinfo=deque([])
maxi=1

for y in range(n):
    for x in range(n):
        allinfo.append((sheet[y][x],y,x))
allinfo=deque(sorted(allinfo))

while allinfo:
    z,y,x=allinfo.popleft()
    val(y,x,z)
print(maxi)


#
# def bfs(y,x,step):
#     maxi=0
#     visited[y][x]=sheet[y][x]
#     q=deque([(y,x,step)])
#     while q:
#         y,x,step=q.pop()
#         if step>maxi:
#             maxi=step
#         else:
#             continue
#         for i in [1,0],[-1,0],[0,-1],[0,1]:
#             ny=y+i[0]
#             nx=x+i[1]
#             if -1<ny<n and -1<nx<n and sheet[ny][nx]>visited[y][x]:
#                 q.append((ny,nx,step+1))
#                 visited[ny][nx]=sheet[ny][nx]
#     return maxi
#
# n=int(input())
#
# sheet=[[int(x) for x in input().split()]for y in range(n)]
# visited=[[0 for x in range(n)]for y in range(n)]
# big=0
#
# for y in range(n):
#     for x in range(n):
#         k=bfs(y,x,1)
#         if k>big:
#             big=k
#
# print(big)

