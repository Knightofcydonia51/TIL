import sys
sys.stdin=open('NM01.txt')

T=int(input())
for i in range(T):
    s = []
    def printPerm(M, string):
        s.append(string)

    def perm(n, k, string):
        if M == k:
            printPerm(M, string)
        else:
            for i in range(k, n):
                A[i], A[k] = A[k], A[i]
                perm(n, k+1, string + data[A[k]]+" ")
                A[i], A[k] = A[k], A[i]

    N, M = map(int, input().split())

    A = [i for i in range(N)]
    data = [str(i) for i in range(1, N+1)]
    print(A)
    print(data)

    perm(N, 0, "")
    s.sort()
    for i in range(len(s)):
        print(s[i])





# s = []
# def PrintArr(n,string):
#     s.append(string)
#
# def perm(n, k, string):
#     if n-1 == k:
#         string = data[0] + string + data[len(data)-1]
#         PrintArr(n, string)
#     else:
#         for i in range(k, n-1):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k+1, string + data[arr[k]])
#             arr[k], arr[i] = arr[i], arr[k]
# N = 5
# arr = [i for i in range(N)]
# data = [str(i) for i in range(1,N+1)]
# perm(N, 1, "")
#
# for i in range(len(s)):
#     print(s[i])