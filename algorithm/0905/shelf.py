import sys
sys.stdin = open('shelf.txt', 'r')

def powerset(n,k,cursum):
    global ans
    if ans<cursum:return
    if n==k:
        if cursum>=B:
            if cursum<ans:
                ans=cursum
            return
    else:
        powerset(n,k+1,cursum+heights[k])
        powerset(n, k + 1, cursum)

T=int(input())

for i in range(T):
    N,B=map(int,input().split())
    heights=[int(x) for x in input().split()]
    A=[0]*N
    ans=999999
    powerset(N,0,0)

    print('#{} {}'.format(i+1,ans-B))