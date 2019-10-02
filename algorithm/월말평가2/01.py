import sys
sys.stdin=open('01.txt')

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    farm = [[0 for x in range(N)] for y in range(N)]
    maxi=0
    cnt=0
    for k in range(M):
        jump=[int(x) for x in input().split()]# 1 1 2 3 0 아래 아래 왼 오 위
        #좌표(y,x), 방향, 점프 거리
        if jump[2]==0: #위
            for y in range(jump[0],-1,-jump[3]):
                farm[y][jump[1]] += 1
                if farm[y][jump[1]]>cnt:
                    cnt=farm[y][jump[1]]
        elif jump[2]==1: #아래
            for y in range(jump[0],N,jump[3]):
                farm[y][jump[1]]+=1
                if farm[y][jump[1]]>cnt:
                    cnt=farm[y][jump[1]]
        elif jump[2]==2: #좌
            for x in range(jump[1],-1,-jump[3]):
                farm[jump[0]][x]+=1
                if farm[jump[0]][x]>cnt:
                    cnt=farm[jump[0]][x]
        elif jump[2]==3: #우
            for x in range(jump[1],N,jump[3]):
                farm[jump[0]][x]+=1
                if farm[jump[0]][x]>cnt:
                    cnt=farm[jump[0]][x]
    for y in range(N):
        for x in range(N):
            if farm[y][x]==cnt:
                maxi+=1
    print('#{} {} {}'.format(i+1,cnt,maxi))

