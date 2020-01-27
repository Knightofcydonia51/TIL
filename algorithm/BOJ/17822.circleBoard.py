from collections import deque as deq
import sys
sys.stdin=open('17822.circleBoard.txt')


N,M,T = map(int,input().split())
board=[deq(int(x) for x in input().split()) for y in range(N)]

for i in range(T):
    num, direc, kan =  map(int,input().split())
    for k in range(N):
        if (k+1)%num==0:
            if direc==0: # 시계방향
                for j in range(kan):
                    board[k].appendleft(board[k].pop())
            else: # 반시계
                for j in range(kan):
                    board[k].append(board[k].popleft())

    val=0
    change=[] # 0이 될 좌표
    for y in range(N):
        for x in range(M):
            if y<N-1:
                if x<M-1:
                    if board[y][x+1]==board[y][x] and board[y][x+1]!=0:
                        change.append((y,x + 1))
                        change.append((y,x))
                        val += 1
                    if board[y+1][x]==board[y][x] and board[y+1][x]!=0:
                        change.append((y+1, x))
                        change.append((y, x))
                        val += 1
                elif x==M-1:
                    if board[y][0]==board[y][x] and board[y][0]!=0:
                        change.append((y, 0))
                        change.append((y, x))
                        val += 1
                    if board[y+1][x]==board[y][x] and board[y+1][x]!=0:
                        change.append((y+1, x))
                        change.append((y, x))
                        val += 1
            elif y==N-1:
                if x < M - 1:
                    if board[y][x + 1] == board[y][x] and board[y][x+1]!=0:
                        change.append((y, x + 1))
                        change.append((y, x))
                        val += 1
                else:
                    if board[y][0] == board[y][x] and board[y][0]!=0:
                        change.append((y, 0))
                        change.append((y, x))
                        val += 1
    ans=0
    numbers=0
    while change:
        y,x=change.pop()
        board[y][x]=0
    for y in range(N):
        for x in range(M):
            ans+=board[y][x]
            if board[y][x]>0:
                numbers+=1

    if val>0:
        pass
    else:
        if numbers==0:
            avg=0
        else:
            avg=ans / numbers
        ans=0
        for y in range(N):
            for x in range(M):
                if board[y][x]>0:
                    if board[y][x]<avg:
                        board[y][x]+=1
                        ans+=board[y][x]
                    elif board[y][x]>avg:
                        board[y][x]-=1
                        ans+=board[y][x]
                    else:
                        ans += board[y][x]
print(ans)

