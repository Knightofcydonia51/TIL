import sys
sys.stdin=open('minimum.txt')

def dfs(y,x,cnt):
    global mini

    if cnt>=mini:return

    if y==N-1 and x==N-1:
        if cnt<mini:
            mini=cnt

    for k in range(2):
        testy=y+dy[k]
        testx=x+dx[k]
        if testy<N and testx<N:
            dfs(testy,testx,cnt+sheet[testy][testx])

dx=[0,1]
dy=[1,0]

T= int(input())
for i in range(T):
    N=int(input())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    mini=999999
    dfs(0,0,sheet[0][0])
    print('#{} {}'.format(i+1,mini))