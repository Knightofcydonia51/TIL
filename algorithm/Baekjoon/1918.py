import sys
sys.stdin=open("tomato.txt")
def comb(r,k):
    if r==3:
        for i in range(len(T)):
            print(T[i],end=" ")
        print()
    if k>len(data)-1 or r>len(T)-1:
        return
    else:
        T[r]=data[k]
        comb(r+1,k+1)
        comb(r,k+1)


data=[int(x) for x in range(6)]
T=[0]*3
comb(0,0)

ans= -1
N=int(input())
people=[int(x) for x in input().split()]
node=[list(map(int, input().split())) for _ in range(N)]
