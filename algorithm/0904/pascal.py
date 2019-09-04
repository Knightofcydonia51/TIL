import sys
sys.stdin=open("pascal.txt")

T=int(input())

for i in range(T):
    N=int(input())
    tri=[[0 for x in range(y)]for y in range(1,N+1)]
    tri[0][0]=1
    for y in range(1,N):
        for x in range(len(tri[y])):
            if x==0 or x==len(tri[y])-1:
                tri[y][x]=1
            else:
                tri[y][x]=tri[y-1][x-1]+tri[y-1][x] #[2][1] = [1][0]+ [1][1]   [3][1]=[2][0]+[2][1]

    print('#{}'.format(i+1))
    for j in range(len(tri)):
        if j==0:
            pass
        else:
            print()
        for k in tri[j]:
            print(k,end=" ")
    print()