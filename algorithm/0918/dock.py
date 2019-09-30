import sys
sys.stdin=open('dock.txt')

T = int(input())
for i in range(T):
    N=int(input())
    time=[[int(x) for x in input().split()]for y in range(N)]
    time.sort(key=lambda x:x[1])
    cnt=0
    end=0
    for k in range(len(time)):
        if time[k][0]>=end:
            cnt+=1
            end=time[k][1]
    print('#{} {}'.format(i+1,cnt))

