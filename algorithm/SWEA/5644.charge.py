
dx=[0,0,1,0,-1]
dy=[0,-1,0,1,0]

T=int(input())
for i in range(T):
    sheet = [[0 for x in range(10)] for y in range(10)]
    M,A=map(int,input().split())
    amove=[int(x) for x in input().split()]
    bmove=[int(x) for x in input().split()]
    for j in range(A):
        input()