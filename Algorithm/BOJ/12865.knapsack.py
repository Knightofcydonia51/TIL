import sys
sys.stdin=open('12865.knapsack.txt')




N,K=map(int,input().split())
stuffs=[list(map(int,input().split())) for x in range(N)]
dp=[[0 for x in range(K+1)]for y in range(N+1)]
# N : 물건 개수  K : 배낭 크기
for k in range(1,N+1):
    for j in range(K+1):
        # j가 k번째 물건의 무게와 같아지기 시작할 때부터 끝까지
        weight,value=stuffs[k-1]
        if j>=stuffs[k-1][0]:
            dp[k][j]=max(dp[k-1][j-weight]+value,dp[k-1][j])
        else:
            dp[k][j]=dp[k-1][j]
print(max(dp[-1]))
