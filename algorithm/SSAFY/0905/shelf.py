import sys
sys.stdin = open('shelf.txt', 'r')

T=int(input())

def powerset(n,k,cursum):
    global mini
    if cursum>=mini:return
    if n==k:
        if cursum>=B:
            if cursum<mini:
                mini=cursum
    else:
        A[k]=1
        powerset(n,k+1,cursum+heights[k])
        A[k]=0
        powerset(n,k+1,cursum)

for i in range(T):
    N,B=map(int,input().split())
    heights=[int(x) for x in input().split()]
    mini=99999
    A=[0]*N
    powerset(N,0,0)
    print('#{} {}'.format(i+1,mini-B))
    #B이상이면서 최소
    #부분집합으로 풀것