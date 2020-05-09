import sys
sys.stdin=open('mst_cal.txt')

def bfs(n,m):

    visit[n]=1
    queue=[n]
    while len(queue)!=0:
        n=queue.pop(0)
        cal=[n+1,n-1,n*2,n-10]
        for i in range(4):
            if cal[i] == m:
                return visit[n]
            if 1000000>=cal[i]>0 and visit[cal[i]]==0:
                visit[cal[i]]=visit[n]+1
                queue.append(cal[i])
T=int(input())

for i in range(T):
    N, M =map(int,input().split())
    visit=[0 for x in range(1000001)]
    print('#{} {}'.format(i+1,bfs(N,M)))
