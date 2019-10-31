import sys
sys.stdin=open('9205.Beer.txt')


def bfs(v):
    global flag
    q=[]
    q.append(v)
    visit[v]=1
    while q:
        v=q.pop(0)
        if v==len(A)-1:
            flag='happy'
            break
        for j in range(1,n+2):
            if G[v][j]==1 and visit[j]==0:
                q.append(j)
                visit[j]=1

t=int(input())

for i in range(t):
    n=int(input())
    A=[[int(x) for x in input().split()] for y in range(n+2)]
    visit=[0 for x in range(n+2)]
    G=[[0 for x in range(n+2)]for y in range(n+2)]

    for j in range(len(A)):
        print(A[j])
    print()

    for j in range(0,len(A)-1):
        for k in range(j,len(A)-1):
            if A[k+1][0]-A[k][0]+A[k+1][1]-A[k][1]<=1000:
                G[]

            # if A[k+1][0]-A[k][0]+A[k+1][1]-A[k][1]<=1000:
            #     G[k][k+1]=1
            #     G[k+1][k] = 1

    for j in range(len(G)):
        print(j, G[j])
    print()

    flag='sad'
    bfs(0)
    print(flag)








