import sys
sys.stdin=open('knapsack.txt')

T=int(input())


for i in range(T):
    N, M=map(int,input().split())
    stuffs=[list(map(int,input().split())) for x in range(M)]
    dp=[[0 for x in range(N+1)]for y in range(M+1)]
    # N : 가방의 크기  M : 물건 개수
    for k in range(1,M+1):
        for j in range(N+1):
            # j가 k번째 물건의 무게와 같아지기 시작할 때부터 끝까지
            if j>=stuffs[k-1][0]:
                dp[k][j]=max(dp[k-1][j-stuffs[k-1][0]]+stuffs[k-1][1],dp[k-1][j])
            else:
                dp[k][j]=dp[k-1][j]
    print('#{} {}'.format(i+1,max(dp[-1])))
