import sys
sys.stdin = open('shelf.txt', 'r')

def perm(n,k,cursum):
    global ans
    if ans<cursum:return

    if n == k:
        if cursum >= B:
            if ans > cursum:
                ans = cursum
                return
    else:
        arr[k] = 1
        perm(n, k + 1, cursum + heights[k])
        arr[k] = 0
        perm(n, k + 1, cursum)

T=int(input())

for i in range(T):
    N,B=map(int,input().split())
    heights=[int(x) for x in input().split()]
    ans=0xfffffff
    arr=[0]*N
    for j in range(N):
        arr[j]=j
    perm(N,0,0)
    print('#{} {}'.format(i+1,ans-B))
