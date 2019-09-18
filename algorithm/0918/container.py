import sys
sys.stdin=open('container.txt')

def comb(n,r):
    global maxi
    if sum(A)<maxi:return
    if r==0:
        if sum(A)>maxi:
            maxi=sum(A)
    else:
        if n<r:return
        else:
            if truck[r-1]>=con[n-1]:
                A[r-1]=con[n-1]
            comb(n-1,r-1)
            comb(n - 1, r)

T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    con=[int(x) for x in input().split()]
    truck=[int(x) for x in input().split()]
    A=[0]*M
    maxi=0
    comb(N,M)
    print(maxi)