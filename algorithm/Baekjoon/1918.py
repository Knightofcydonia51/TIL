
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

