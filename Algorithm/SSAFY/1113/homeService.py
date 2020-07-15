import sys
sys.stdin=open('homeService.txt')

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    maxi=0
    for k in range(1,N+2): # k 정해주고
        cost=k*k+(k-1)*(k-1)
        for y in range(N): # 가운데 점의 y위치
            for x in range(N): # 가운데의 x위치
                home=0
                money=0
                end=0
                start=1
                step=1
                for j in range(-k+1+y,k+y): # 0,1 -1,2 -2,3 -1,2 0,1
                    #m의 범위변경:

                    # end = 1 2 3 2 1  1씩 k까지 1 2 3 4 5 6
                    end+=step
                    # start = 0부터 -k-1까지 감소 0 -1 -2 -3 -4
                    start-=step
                    if end==k+1:
                        step=(-1)
                        end += (step*2)
                        start -= (step*2)
                    for m in range(start+x,end+x,1):

                        if N>j>-1 and N>m>-1:

                            if sheet[j][m]==1:
                                money+=M
                                home+=1
                if money>=cost:
                    if home>maxi:
                        maxi=home

    print('#{} {}'.format(i+1,maxi))









