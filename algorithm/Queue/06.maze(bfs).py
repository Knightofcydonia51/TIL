import sys
sys.stdin = open('06.maze(bfs).txt', 'r')

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(y,x):
    global flag
    global result
    queue=[]
    queue.append(y)
    queue.append(x)
    visited[y][x]=1
    while len(queue)!=0:
        tempy=queue.pop(0)
        tempx=queue.pop(0)
        w=visited[tempy][tempx]
        if maze[tempy][tempx]==3:
            flag=1
            result.append(tempy)
            result.append(tempx)
            break
        for j in range(4):
            testx=tempx+dx[j]
            testy=tempy+dy[j]
            if N>testx>-1 and N>testy>-1 and visited[testy][testx]==0 and maze[testy][testx]!=1:
                queue.append(testy)
                queue.append(testx)
                visited[testy][testx]=w+1

T=int(input())

for i in range(T):
    N=int(input())
    maze=[[int(x) for x in input()]for y in range(N)]
    visited=[[0 for x in range(N)]for y in range(N)]

    flag=0
    result=[]
    for y in range(len(maze)):
        for x in range(len(maze)):
            if maze[y][x]==2 and visited[y][x]==0:
                bfs(y , x)
    if flag==1:
        print("#{} {}".format(i+1,visited[result[0]][result[1]] - 2))
    else:
        print("#{} 0".format(i+1))