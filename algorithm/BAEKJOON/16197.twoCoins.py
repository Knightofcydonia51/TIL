import sys
sys.stdin=open('16197.twoCoins.txt')

def start():
    for y in range(N):
        for x in range(M):
            if board[y][x]=='o':
                coins.append((y,x))
            if len(coins)==2:
                return

def dfs(y1,x1,y2,x2,step):
    global mini
    if step>10:
        return
    for i in [(-1,0),(1,0),(0,-1),(0,1)]:
        flag = 0
        ny1=y1+i[0]
        nx1=x1+i[1]
        ny2=y2+i[0]
        nx2=x2+i[1]
        if -1<ny1<N and -1<nx1<M:
            if board[ny1][nx1]=='#':
                ny1,nx1=y1,x1
        else:
            flag+=1

        if -1<ny2<N and -1<nx2<M:
            if board[ny2][nx2]=='#':
                ny2, nx2 = y2, x2
        else:
            flag+=1

        if flag==2:
            continue
        if flag==1:
            if step+1<mini:
                mini=step+1
        else:
            dfs(ny1,nx1,ny2,nx2,step+1)


N ,M=map(int,input().split())
board=[[x for x in input()]for y in range(N)]
visit=[[0 for x in range(M)]for y in range(M)]
coins=[]
start()
mini= 11
dfs(coins[0][0],coins[0][1],coins[1][0],coins[1][1],0)
if mini==11:
    mini= -1
print(mini)




