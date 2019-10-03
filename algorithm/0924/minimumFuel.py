# import time
# start_time = time.time()
import sys
sys.stdin=open('minimumFuel.txt')

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(y,x):
    global mini
    global flag
    queue=[]
    queue.append((y,x,sheet[y][x]))
    D[0][0]=0
    while queue:
        nyx=queue.pop(0)
        for i in range(4):
            ny = nyx[0]+dy[i]
            nx = nyx[1]+dx[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                diff=0
                if nyx[2]<sheet[ny][nx]:
                    diff=sheet[ny][nx]-nyx[2]
                if D[ny][nx] > (D[nyx[0]][nyx[1]] + diff + 1):
                    D[ny][nx] = D[nyx[0]][nyx[1]] + diff + 1
                    queue.append((ny, nx,sheet[ny][nx]))
    return D[N - 1][N - 1]

T=int(input())

for i in range(T):
    N=int(input())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    D = [[987654321] * N for i in range(N)]
    print('#{} {}'.format(i+1,bfs(0,0)))
# print(time.time() - start_time, 'seconds')
