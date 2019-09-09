


T=int(input())

for i in range(T):
    N=int(input())
    temp=list(map(int,input().split()))
    A=[0]+list(range(1,N+1,1)) + [N+1]
    P=[(0,0) for x in range(N+2)]
    D=[[0 for x in range(N+2)] for y in range(N+2)]
    ans=0x7fffffff
    P[0]=(temp[0], temp[1])
    P[N+1]=(temp[2],temp[3])









