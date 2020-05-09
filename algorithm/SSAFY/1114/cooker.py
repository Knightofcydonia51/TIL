import sys
sys.stdin=open('cooker.txt')

def comb(n,r,q):
    global mini

    if r==0:
        com1=[]
        com2=[]
        for i in range(q):
            com1.append(T[i])
        for i in range(len(A)):
            if i not in com1:
                com2.append(i)

        partA=0
        partB=0
        for y in range(num):
            for x in range(y+1,num):
                partA+=food[com1[y]][com1[x]]+food[com1[x]][com1[y]]
                partB+=food[com2[y]][com2[x]]+food[com2[x]][com2[y]]
        ans=abs(partA-partB)
        if ans<mini:
            mini=ans

    else:
        if n<r:
            return
        else:
            T[r-1]=A[n-1]
            comb(n-1,r-1,q)
            comb(n - 1, r, q)

T=int(input())

for i in range(T):
    N=int(input())
    food=[[int(x) for x in input().split()]for y in range(N)]
    mini=999999
    num=len(food) // 2
    A=[int(x) for x in range(num*2)]
    T=[0]*num
    comb(num*2,num,num)
    print('#{} {}'.format(i+1,mini))



