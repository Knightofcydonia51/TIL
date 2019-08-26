import sys
sys.stdin=open("09.Farm.txt",  'rt', encoding='UTF8')

T=int(input())

for i in range(T):
    N=int(input())
    map=[[int(x) for x in input()]for y in range(N)]
    step=1
    j=(-1)
    ans=0
    end=(-1)
    start = ((N - 1) // 2)+1
    for k in range(N): #3 2 1 0 1 2 3
        end+=2*(-j)
        start+=j
        for u in range(0,end,step): #  1 3 5..N..5 3 1
            ans+=map[k][start+u]
        if start == 0:
            j = 1
    print("#{} {}".format(i+1,ans))
