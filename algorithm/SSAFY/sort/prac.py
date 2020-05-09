'''
합이 10이 되는 부분집합 모두 출력하기
'''
N=10
num=[1,2,3,4,5,6,7,8,9,10]
A=[0]*10
total=0
count=0

def printSet(n):
    global count
    sum=0
    for i in range(n): # 각 부분 배열의 원소 출력
        if A[i]==1:    # A[i]가 1이면 포함된 것이므로 출력.
            sum+=num[i]

    if sum==10:
        count+=1
        print("%d :  " % count,end="")
        for i in range(n):
            if A[i]==1:
                print("%d " % num[i], end="")
        print()

def powerset(n,k):
    global total
    # if sum>10:return 가지치기
    total+=1
    if n==k:
        printSet(n)
    else:
        A[k]=1
        powerset(n,k+1)
        A[k]=0
        powerset(n,k+1)

powerset(N,0)


