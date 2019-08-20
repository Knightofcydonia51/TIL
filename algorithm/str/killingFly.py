import sys
sys.stdin=open("killingFly.txt")

T=int(input())
for i in range(T):
    NM=[int(x) for x in input().split()]
    N=int(NM[0])
    M=int(NM[1])
    sheet=[[int(x) for x in input().split()] for x in range(N)]
    max=0
    kill = 0
    for k in range(N-M+1):
        for j in range(N-M+1):
            if kill>max:
                max=kill
            kill = 0
            for u in range(M):
                for m in range(M):
                    kill+=sheet[u+k][m+j]
    print('#{} {}'.format(i+1, max))
