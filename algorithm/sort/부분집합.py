import time
start_time = time.time()

N=3
A=[0 for x in range(N)]
data=[x for x in range(1,N+1)]


def printSet(n):
    for i in range(n): # 각 부분 배열의 원소 출력
        if A[i]==1: # A[i]가 1이면 포함된 것이므로 출력.
            print("%d " % data[i], end="")
    print()
def powerset(n,k):
    if n==k:
        printSet(n)
    else:
        A[k]=1
        powerset(n,k+1)
        A[k]=0
        powerset(n,k+1)

powerset(N,0)
print(time.time() - start_time, 'seconds')



