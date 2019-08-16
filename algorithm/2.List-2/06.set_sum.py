import sys
sys.stdin=open("06.set_sum.txt")

T=int(input())

arr=[0]*12
for x in range(1,13):
    arr[x-1]=x

for case in range(T):
    NK=[int(x) for x in input().split()]
    N=NK[0]
    K=NK[1]
    ans=0
    n=len(arr)
    ans=0
    for i in range(1<<n):
        one = []
        for j in range(n+1):
            if i & (1<<j):
                one.append(arr[j])

        if len(one)==N:
            temp = 0
            for v in one:
                temp+=v
            if temp==K:
                ans+=1
    print('#{} {}'.format(case+1, ans))

