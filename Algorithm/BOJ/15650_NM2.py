import sys
sys.stdin=open('15650_NM2.txt')

def comb(n,r,q):
    global block
    if r==0:
        for i in range(q):
            block.append(T[i])
        ans.append(block)
        block=[]

    else:
        if n<r:
            return
        else:
            T[r-1]=A[n-1]
            comb(n-1,r-1,q) #comb(n,r-1,q) 중복조합
            comb(n - 1, r, q)

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    A=[int(x) for x in range(1,N+1)]
    T=[0]*M
    ans=[]
    block=[]
    comb(N,M,M)
    for k in sorted(ans):
        for j in range(len(k)):
            print(k[j],end=" ")
        print()