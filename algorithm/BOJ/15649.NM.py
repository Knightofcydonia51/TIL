import sys
sys.stdin=open("15649.NM.txt")

def perm(n,k):
    global block
    if k==M:
        for k in range(M):
            block+=A[k]+" "
        ans.append(block)
        block=""

    else:
        for i in range(k,n):
            A[i],A[k]=A[k],A[i]
            perm(n,k+1)
            A[i], A[k] = A[k], A[i]

T=int(input())
for i in range(T):
    N,M=map(int,input().split())

    A=[str(x) for x in range(1,N+1)]
    block=""
    ans=[]

    perm(N,0)
    ans.sort()
    for k in range(len(ans)):
        print(ans[k])
    print()


def comb(n,r,q):
    if r==0:
        for i in range(q):
            print("{}".format(T[i]),end=" ")
        print()
    else:
        if n<r:
            return
        else:
            T[r-1]=A[n-1]  # 여기서 무조건 T에 A의 r자리에 존재하는 수를 넣어줌. [0, 0, 6]
            comb(n-1,r-1,q) # 선택 했을 경우 [0, 5, 6]             comb(n,r-1,q) 중복조합
            comb(n - 1, r, q) # 선택 안했을 경우 [0, 0, 5]

A=[1,2,3,4,5,6]
T=[0]*3

comb(6,3,3)
# n은 고르고자 하는 자리의 번호(이후 하나씩 줄어듬 ex) 6에서부터 1까지 )
# r은 현재 스탭에서 몇개를 골랐는지를 나타냄(0이 됐다면 다 고른거.)
# q는 최종적으로 뽑는 수를 나타냄. 3이면 결국 3개를 뽑겠다는 뜻.


