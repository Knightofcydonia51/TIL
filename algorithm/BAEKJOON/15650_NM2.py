import sys
sys.stdin=open('15650_NM2.txt')




def perm(n,k):
    if M==k:
        for i in range(M):
            print(A[i],end=" ")
        print()
    else:
        for i in range(k,n):
            A[k],A[i]=A[i],A[k]
            perm(n,k+1)
            A[k], A[i] = A[i], A[k]


T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    print(N,M)
    A=[int(x) for x in range(1,N+1)]
    ans=[]
    perm(N,0)
    print(ans)
