def comb(n,r,q):
    if r==0:
        for i in range(q):
            print("{}".format(T[i]),end=" ")
        print()
    else:
        if n<r:
            return
        else:
            T[r-1]=A[n-1]
            comb(n-1,r-1,q)
            comb(n - 1, r, q)

A=[1,2,3,4]
T=[0]*3

comb(4,3,3)