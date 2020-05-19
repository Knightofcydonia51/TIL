import sys
sys.stdin=open('minimumCost.txt')



def perm(n,k,cursum):
    global minnum
    if cursum>=minnum:return
    if n==k:
        if minnum>cursum:
            minnum=cursum
    else:
        for i in range(k,n):
            A[i],A[k]=A[k],A[i]
            perm(n,k+1,cursum+cost[k][A[k]])
            A[i], A[k] = A[k], A[i]

T=int(input())
for i in range(T):
    N=int(input())
    cost=[[int(x) for x in input().split()]for y in range(N)]
    A=[i for i in range(N)]
    minnum=99999
    perm(N,0,0)
    print('#{} {}'.format(i+1,minnum))