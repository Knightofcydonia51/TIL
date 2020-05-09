import sys
sys.stdin = open('distribute.txt', 'r')

def perm(n,k,maxi):
    global ans
    if ans>=maxi:return
    if k==n:
        if ans<maxi:ans=maxi
    else:
        for i in range(k,n):
            arr[k], arr[i]= arr[i], arr[k]
            perm(n,k+1,maxi*(works[k][arr[k]])*0.01)
            arr[k], arr[i] = arr[i], arr[k]
T=int(input())

for i in range(T):
    N=int(input())
    works=[[int(x) for x in input().split()]for y in range(N)]
    ans=0
    arr=[0]*N
    for j in range(N):
        arr[j]=j
    perm(N,0,1)
    # ans=round(ans*100,6)
    print('#{} {:6f}'.format(i+1,ans*100))