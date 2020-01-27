import sys
sys.stdin=open('2309.dwarfs.txt')

def comb(r,k):
    global flag
    if 9-k<7-r or flag==1:return
    if r==7:
        ans=0
        for i in range(7):
            ans+=A[i]
        if ans==100:
            for k in sorted(A):
                print(k)
            flag=1
    else:
        if r<7 and k<9:
            A[r]=data[k]
            comb(r+1,k+1)
            comb(r,k+1)

A=[int(x) for x in range(7)]
data=[int(input()) for x in range(9)]
flag=0
comb(0,0)
