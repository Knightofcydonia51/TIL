count=0
N=3
A=[0 for _ in range(N)]
data=[1,2,3]

print(A)
def printSet(n):
    global count
    count+=1
    print("%d : " % (count), end="") #부분 집합의 갯수 출력
    for i in range(n): #각 부분집합의 원소 출력
        if A[i]==1: #A[i]가 1이면 포함된 것이므로 출력.
            print("%d " % data[i],end="")
    print()

def powerset(n,k): #n:원소의 갯수, k:현재 depth
    if n==k:
        printSet(n)
    else:
        A[k]=1
        powerset(n, k+1)
        A[k]=0
        powerset(n, k+1)

powerset(N, 0)