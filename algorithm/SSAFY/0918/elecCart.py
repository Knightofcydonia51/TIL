import sys
sys.stdin=open('elecCart.txt')

def perm(n,k,q):
    global mini
    if q>=mini:return
    if n==k:
        q+=sheet[A[-1]][0]
        if mini>q:
            mini=q
    else:
        for i in range(k,n):
            A[i],A[k]=A[k],A[i]
            perm(n,k+1,q+sheet[A[k-1]][A[k]])
            A[i], A[k] = A[k], A[i]


T=int(input())
for i in range(T):
    N=int(input())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    A=[int(x) for x in range(N)]
    mini=98765
    perm(N,1,0)
    print(mini)




# def perm(n,k):
#     global mini
#     hap=0
#     if arr[0]!=0:return
#     if n==k:
#         for j in range(N-1):
#             hap+=sheet[arr[j]][arr[j+1]]
#         hap+=sheet[arr[N-1]][arr[0]]
#         if mini>hap:
#             mini=hap
#
#     else:
#         for i in range(k,n):
#             arr[k],arr[i]=arr[i],arr[k]
#             perm(n,k+1)
#             arr[k], arr[i] = arr[i], arr[k]
#
# T=int(input())
# for i in range(T):
#     N=int(input())
#     mini=99999
#     arr=[i for i in range(N)]
#     sheet=[[int(x) for x in input().split()]for y in range(N)]
#     perm(N,0)
#     print('#{} {}'.format(i+1,mini))


