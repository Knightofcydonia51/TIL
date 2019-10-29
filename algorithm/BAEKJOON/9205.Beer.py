import sys
sys.stdin=open('9205.Beer.txt')

def perm(n,k):
    global flag
    if flag==1:
        flag='happy'
        return
    if n==k:
        for j in range(len(A)-1):
            if A[j+1][0]-A[j][0]+A[j+1][1]-A[j][1]<=1000:
                if j==len(A)-2:
                    flag=1
                continue
            else:
                break

    for j in range(k,n):
        A[k],A[j]=A[j],A[k]
        perm(n,k+1)
        A[k], A[j] = A[j], A[k]

t=int(input())

for i in range(t):
    n=int(input())
    A=[[int(x) for x in input().split()] for y in range(n+2)]
    flag='sad'
    perm(len(A)-1, 1)
    print(flag)






