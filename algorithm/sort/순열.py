#
# a=[1,2,3,4]
# t=[0]*3
# def myprint(q):
#     for i in range(q):
#         print("%d " % t[i], end="")
#     print()
#
# def perm(n,k,q):
#     if n==k:
#         myprint(q)
#     else:
#         for i in range(n-1, -1, -1):
#             a[i],a[n-1]=a[n-1],a[i]
#             t[r-1] = a[n-1]
#             perm(n-1,r-1,q) #perm(n,r-1,q) 중복순열
#             a[i], a[n - 1] = a[n - 1], a[i]
#
# perm(4,2,2)

def PrintArr(n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def perm(n,k):
    if k==n:
        PrintArr(n)
    else:
        for i in range(k,n):
            arr[k], arr[i]=arr[i],arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr=[1,2,3]
perm(3, 0)
