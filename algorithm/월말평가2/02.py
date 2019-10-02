import sys
sys.stdin=open('02.txt')

def perm(n,k):
    global maxi
    if k==3:
        ans = 0
        ans+=abs(six[A[2]] - six[A[0]])
        for j in range(2):
            ans+=abs(six[A[j]]-six[A[j+1]])
        if ans>maxi:
            maxi=ans
        else:return
    else:
        for i in range(k,n):
            A[k],A[i]=A[i],A[k]
            perm(n,k+1)
            A[k], A[i] = A[i], A[k]

T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    A=[x for x in range(6)]
    maxi = 0
    for k in range(1,N): #N회(행)
        for j in range(1,M): #M!회(열)
            for u in range(j+1,M):
                six = [0 for x in range(6)]
                for y in range(k):
                    for x in range(j):
                        six[0]+=sheet[y][x]
                for y in range(k):
                    for x in range(j,u):
                        six[1]+=sheet[y][x]
                for y in range(k):
                    for x in range(u,M):
                        six[2]+=sheet[y][x]
                for y in range(k,N):
                    for x in range(j):
                        six[3]+=sheet[y][x]
                for y in range(k,N):
                    for x in range(j, u):
                        six[4]+=sheet[y][x]
                for y in range(k, N):
                    for x in range(u, M):
                        six[5] += sheet[y][x]
                perm(6,0)

    print('#{} {}'.format(i+1,maxi))


