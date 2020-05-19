

def perm(n,k,q):
    global min
    if q>min:
        return
    if k==3:
        if q<=min:
            min=q
    else:
        for i in range(k,n):
            A[k],A[i]=A[i],A[k]
            perm(n,k+1,q+data[A[k]])
            A[k], A[i] = A[i], A[k]

data=[10,2,1,3]
A=[0,1,2,3]
min=9876
perm(4,0,0) #목표로 하는 리스트의 길이, 자리바꿔주는 역할을 하는 리스트의 길이, 뽑고싶은 수
print(min)

