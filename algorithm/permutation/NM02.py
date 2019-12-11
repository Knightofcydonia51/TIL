import sys
sys.stdin=open('NM02.txt')

def comb(r,k):
    if N-k<M-r:return #고를 수 있는 숫자 개수가 만약 남은 칸의 개수보다 적다면? 볼 필요가 없음.
    if r==M:
        for i in range(M):
            print(t[i], end=" ")
        print()
    else:
        if r<M and k<N:
            t[r]=data[k]
            comb(r+1,k+1)
            comb(r,k+1)

T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    data=list(range(1,N+1))
    t=[0]*M
    ans=[]
    comb(0,0) # n:자리의 번호 r:현재 스탭에서 몇개를 골랐는지 q:M(최종적으로 뽑고싶은 갯수)


# import sys
# sys.stdin=open('NM01.txt')
#
# def perm(k):
#     if k==M:
#         for i in range(M):
#             print(A[i], end=" ")
#         print()
#     else:
#         for i in range(k,N):
#             A[i], A[k]= A[k], A[i]
#             perm(k+1)
#             A[i], A[k] = A[k], A[i]
# T=int(input())
# for i in range(T):
#     N,M=map(int,input().split())
#     A=[int(x) for x in range(1,N+1)]
#     perm(0)

# import sys
# sys.stdin=open('NM01.txt')
#
# def comb(N,M,k,arr):
#     if k==M:
#         tem = sorted(arr)
#         if tem not in check:
#             check.append(tem)
#             for a in range(len(arr)):
#                 print(arr[a], end=" ")
#             print()
#     else:
#         for i in range(1,N+1):
#             if i not in arr:
#                 comb(N,M,k+1,arr+[i])
# T=int(input())
# for i in range(T):
#     N, M = map(int, input().split())
#     check = []
#     comb(N,M,0,[])