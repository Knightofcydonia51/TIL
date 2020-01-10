import sys
sys.stdin=open('1987.alphabet.txt')
import collections

dyx=[[1,0],[-1,0],[0,-1],[0,1]]

def bfs(y,x):
    global maxi
    q=collections.deque([(y,x,str(sheet[0][0]),1)])
    while q:
        y,x,check,step=q.popleft()
        for i in range(4):
            ny=dyx[i][0]+y
            nx=dyx[i][1]+x
            if -1<ny<R and -1<nx<C and sheet[ny][nx] not in check:
                if path[ny][nx]==check+sheet[ny][nx]:
                    continue
                else:
                    q.append((ny,nx,check+sheet[ny][nx],step+1))
                    path[ny][nx]=check+sheet[ny][nx]
                    if step+1>maxi:
                        maxi=step+1


R, C = map(int,input().split())

sheet=[[x for x in input()]for y in range(R)]
path=[['' for x in range(C)]for y in range(R)]
path[0][0]=sheet[0][0]
maxi=0
bfs(0,0)
print(maxi)


# from sys import stdin
# import collections
# r, c = map(int, stdin.readline().split())
# board = [stdin.readline() for _ in range(r)]
# cache = [[''] * c for _ in range(r)]
#
# direction = [(-1, 0), (0, 1), (0, -1), (1, 0)]
# q = collections.deque()
# q.append((0, 0, board[0][0]))
# max_len = 1
# while q:
#     y, x, path = q.popleft()
#     for dy, dx in direction:
#         ny = y + dy
#         nx = x + dx
#         if ny < 0 or r <= ny or nx < 0 or c <= nx:
#             continue
#         if board[ny][nx] in path:
#             continue
#         if cache[ny][nx] == path + board[ny][nx]:
#             continue
#         cache[ny][nx] = path + board[ny][nx]
#         q.append((ny, nx, path + board[ny][nx]))
#         max_len = max(max_len, len(path) + 1)
#
# print(max_len)

