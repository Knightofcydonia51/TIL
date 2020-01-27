import sys
sys.stdin=open('1010.bridge.txt')

def comb(r,k):
    global cnt
    if M-k<N-r:return
    if r==N:
        cnt+=1
    else:
        if r<N and k<M:
            A[r]=data[k]
            comb(r+1,k+1)
            comb(r,k+1)

T=int(input())
for i in range(T):
    N, M = map(int,input().split())
    A=[0 for i in range(N)]
    data=[0 for i in range(M)]
    cnt=0
    comb(0,0)
    print(cnt)
