import sys
sys.stdin=open('quick.txt')

def partition(A,l,r):
    p = A[l]
    i = l
    j = r

    while i < j:
        while A[i] <= p:
            i+=1
            if i == r:
                break
        while A[j] >= p:
            j-=1
            if j == l:
                break

        if i<j:
            A[i],A[j]=A[j],A[i]

    A[l],A[j] = A[j], A[l]

    return j

def quickSort(A,l,r):
    if l<r:
        s = partition(A,l,r)
        quickSort(A,l,s-1)
        quickSort(A,s+1,r)

T=int(input())
for i in range(T):
    N=int(input())
    unsorted=[int(x) for x in input().split()]
    quickSort(unsorted,0,len(unsorted)-1)
    print('#{} {}'.format(i+1,unsorted[N//2]))