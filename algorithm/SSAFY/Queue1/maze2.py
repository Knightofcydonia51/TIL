import sys
sys.stdin=open("maze2.txt")

dy=[1,-1,0,0]
dx=[0,0,-1,1]

def bfs(y,x):
    global flag
    visited[y][x]=1
    queue=[]
    queue.append(y)
    queue.append(x)
    while len(queue)!=0:
        tempy=queue.pop(0)
        tempx=queue.pop(0)
        for i in range(4):
            testy=tempy+dy[i]
            testx=tempx+dx[i]
            if -1<testy<100 and -1<testx<100 and visited[testy][testx]==0 and maze[testy][testx]!=1:
                if maze[testy][testx]==3:
                    flag+=1
                    return
                visited[testy][testx]=1
                queue.append(testy)
                queue.append(testx)

for i in range(10):
    N=int(input())
    maze=[[int(x) for x in input()]for y in range(100)]
    visited=[[0 for x in range(100)]for y in range(100)]

    for j in range(len(maze)):
        for k in range(len(maze)):
            if maze[j][k]==2 and visited[j][k]==0:
                flag=0
                bfs(j,k)
    print(flag)
















# dx=[0,0,-1,1]
# dy=[-1,1,0,0]
#
# def bfs(y,x):
#     global flag
#     visited[y][x]=0
#     queue=[]
#     queue.append(y)
#     queue.append(x)
#     while len(queue)!=0:
#         tempy=queue.pop(0)
#         tempx=queue.pop(0)
#         if maze[tempy][tempx]==3:
#             flag+=1
#             return
#         for i in range(4):
#             testy=tempy+dy[i]
#             testx=tempx+dx[i]
#             if 0<testy<100 and 0<testx<100 and visited[testy][testx]==0 and maze[testy][testx]!=1:
#                 queue.append(testy)
#                 queue.append(testx)
#                 visited[testy][testx]=1
#
#
# for i in range(10):
#     N=input()
#     maze=[[int(x) for x in input()]for y in range(100)]
#     visited=[[0 for x in range(100)]for y in range(100)]
#     flag=0
#     for j in range(len(maze)):
#         for k in range(len(maze)):
#             if maze[j][k]==2 and visited[j][k]==0:
#                 bfs(j,k)
#     print('#{} {}'.format(i+1,flag))