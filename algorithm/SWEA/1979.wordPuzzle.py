import sys
sys.stdin=open("1979.wordPuzzle.txt")

T=int(input())

for i in range(T):
    N,K=map(int,input().split())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    ans=0
    for y in range(N):
        weight=0
        weight2=0
        for x in range(N):
            if sheet[y][x]==1:
                weight+=1
                if weight == K:
                    if x+1<N and sheet[y][x+1]!=1:
                        # print(y,x,weight,i, x+1)
                        ans += 1
                    elif x+1==N:
                        ans+=1
            elif sheet[y][x]==0:
                weight=0
            if sheet[x][y]==1:
                weight2+=1
                if weight2 == K:
                    if x + 1 < N and sheet[x+1][y] != 1:
                        # print(y,x,weight,i, x+1)
                        ans += 1
                    elif x + 1 == N:
                        ans += 1
            elif sheet[x][y]==0:
                weight2=0
    print('#{} {}'.format(i+1,ans))