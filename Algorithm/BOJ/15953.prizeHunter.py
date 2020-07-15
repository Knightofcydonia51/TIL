import sys
sys.stdin=open('15953.prizeHunter.txt')

first= [0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10]

T = int(input())

for i in range(T):
    ans=0
    a, b = map(int, input().split())
    if a<22 and a!=0:
        ans+=first[a]*10000

    if b<32 and b!=0:
        n = 9
        for k in range(1,6):
            if b< 2**k:
                ans+=(2**(n-k+1))*10000
                break
    print(ans)
