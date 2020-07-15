import sys
sys.stdin=open('knapsack(Greed).txt')


def cal(w, v, step):
    global maxi
    if w>N:
        return
    else:
        if v>maxi:
            maxi=v
        if step < M:
            cal(w+knapsack[step][0],v+knapsack[step][1],step+1)
            cal(w, v, step+1)
            return

T=int(input())
for i in range(T):
    N,M=map(int,input().split()) # 배낭 크기, 개수
    knapsack=[list(map(int,input().split())) for x in range(M)] # 무게, 가치
    maxi=0
    cal(0,0,0)
    print("#{} {}".format(i+1,maxi))


