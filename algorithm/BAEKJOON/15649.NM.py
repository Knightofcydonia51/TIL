import sys
sys.stdin=open("15649.NM.txt")

def perm(n,k):
    global block
    if k==M:
        for k in range(M):
            block+=A[k]+" "
        ans.append(block)
        block=""

    else:
        for i in range(k,n):
            A[i],A[k]=A[k],A[i]
            perm(n,k+1)
            A[i], A[k] = A[k], A[i]

T=int(input())
for i in range(T):
    N,M=map(int,input().split())


    A=[str(x) for x in range(1,N+1)]
    block=""
    ans=[]

    perm(N,0)
    ans.sort()
    for k in range(len(ans)):
        print(ans[k])
    print()




