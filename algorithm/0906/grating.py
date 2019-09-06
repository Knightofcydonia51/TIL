import sys
sys.stdin=open('grating.txt')

dy=[-1,1,0,0]
dx=[0,0,-1,1]

def dfs(y,x,num,cnt):

    if cnt==7:
        ans.add(num)
        return

    for z in range(4):
        testy=y+dy[z]
        testx=x+dx[z]
        if -1<testy<4 and -1<testx<4:
            dfs(testy,testx,10*num+sheet[testy][testx],cnt+1)

T=int(input())

for i in range(T):
    sheet=[[int(x) for x in input().split()]for y in range(4)]
    ans = set()
    for y in range(len(sheet)):
        for x in range(len(sheet)):
            dfs(y,x,sheet[y][x],1)
    print('#{} {}'.format(i+1,len(ans)))
