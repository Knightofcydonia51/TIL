import sys
sys.stdin=open('9205.Beer.txt')
import collections

# 1000미터를 초과하면 못감
# G에 모든 좌표들의 인접 여부를 표시
# bfs


def bfs(y,x):
    global fy,fx,ans
    visited[0]=1
    q=collections.deque([(y,x)])
    while q:
        y,x=q.popleft()
        if y==fy and x==fx:
            ans="happy"
            return
        for i in range(1,n+2):
            if abs(y-info[i][1])+abs(x-info[i][0])<=1000 and visited[i]==0:
                q.append((info[i][1],info[i][0]))
                visited[i]=1



t=int(input())

for i in range(t):
    ans="sad"
    n=int(input())
    info=[list(map(int,input().split())) for x in range(n+2)]
    fy,fx=info[-1][1],info[-1][0]
    visited=[0 for x in range(n+2)]
    bfs(info[0][1],info[0][0])
    print(ans)







