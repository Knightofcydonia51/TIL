import sys
sys.stdin=open('10844.stair.txt')

N=int(input())
dp=[0,1,1,1,1,1,1,1,1,1]
dp2=[]

for i in range(N-1):
    for k in range(10):
        if k==0:
            dp2.append(dp[1])
        elif k==9:
            dp2.append(dp[8])
        else:
            dp2.append(dp[k-1]+dp[k+1])
    dp=dp2
    dp2=[]
print(sum(dp)%1000000000)
# 한자리수일때 - 9
# 두자리수일때 - 1개(9) 빼고 다 2개씩 irre=1 (ans-irre)*2 + irre   17
# 세자리수일때 - 2개(9,0) 빼고 다 2개씩 irre=2 (ans-irre)*2 + irre  32
# 네자리수일때 - 3개 (9,9,0) 빼고 다 2개씩    29*2 + 3    61
# 다섯자리수일때 - 6개 빼고 다 2개씩           55*2 + 6


# irre = n-1

# N=1  => ans=9
# N=2  => (ans-1)*2 +1
# N=3  => (ans-2)*2 +2
# N=4  => _(ans-2)*2 +2