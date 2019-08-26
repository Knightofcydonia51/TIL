import sys
sys.stdin=open("03.snail.txt")

T=int(input())
for i in range(T):
    N=int(input())
    arr =[[0 for x in range(N)]for y in range(N)]
    dx=[1,0,-1,0] #우 하 좌 상
    dy=[0,1,0,-1]
    x=0
    y=0
    ghostx=0
    ghosty=0
    pointer=0
    for j in range(1,N**2+1):
        x=ghostx
        y=ghosty
        arr[y][x] = j
        ghostx=x+dx[pointer%4]
        ghosty=y+dy[pointer%4]
        if ghostx<0 or ghostx>=N or ghosty>=N or arr[ghosty][ghostx]!=0:
            pointer+=1
            ghostx=x+dx[pointer%4]
            ghosty = y + dy[pointer % 4]
    print('#{}'.format(i+1))

    for k in arr:
        for m in k:
            print(m, end=" ")
        print("")
    # 숫자 찍고 고스트 이동.
    # 고스트가 만약 조건을 벗어났다면, 핸들을 돌리고 현재 좌표를 전진시킴.





















    # x=0
    # y=0
    # testx = 0
    # testy = 0
    # handle=0
    # length=N
    # dx = [1, 0, -1, 0]
    # dy = [0, 1, 0, -1]
    # for j in range(1,N**2+1):
    #     x=testx
    #     y=testy
    #     arr[y][x] = j
    #     testx=x+dx[handle%4]
    #     testy=y+dy[handle%4]
    #     if testx>=length or testx<0 or testy>=length or arr[testy][testx]!=0:
    #         handle+=1
    #         testx=x+dx[handle%4]
    #         testy=y+dy[handle%4]
    # print('#{}'.format(i+1))
    # for k in arr:
    #     for m in k:
    #         print(m, end=' ')
    #     print()