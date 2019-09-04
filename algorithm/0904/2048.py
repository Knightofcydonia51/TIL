import sys
sys.stdin=open("2048.txt")


T=int(input())
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for i in range(T):
    N,S=input().split()
    N=int(N)
    sheet=[[[int(x),0] for x in input().split()]for y in range(N)]
    if S=='up':S=0
    elif S=='down':S=1
    elif S=='left':S=2
    else:S=3
    if S==0:
        originy=0
        originx=0
        testy=1
        testx=0
        for y in range(1,N):
            originy=y
            for x in range(N):
                y=originy
                for z in range(N):
                    testy=y+dy[0]
                    testx = x + dx[0]
                    if N > testy > -1 and N>testx>-1:
                        if N>testy>-1 and sheet[testy][testx][0]==0:
                            sheet[testy][testx][0]=sheet[y][x][0]
                            sheet[y][x][0]=0
                            y=testy
                            x=testx
                        elif sheet[testy][testx][0]!=sheet[y][x][0]:
                            break
                        elif sheet[testy][testx][0]!=0 and sheet[testy][testx][0]==sheet[y][x][0]:
                            if sheet[testy][testx][1]==0: # 합체
                                sheet[testy][testx][1]=1 # 상태값 변경
                                sheet[testy][testx][0]=sheet[y][x][0]*2
                                sheet[y][x][0]=0
                                break
                            elif sheet[testy][testx][1]==1:
                                break
    elif S==1:
        testy=0
        testx=0
        originy=0
        for y in range(N,-1,-1):
            originy=y
            for x in range(N):
                y=originy
                for z in range(N):
                    testy=y+dy[1]
                    testx = x + dx[1]
                    if N > testy > -1 and N > testx > -1:
                        if N>testy>-1 and sheet[testy][testx][0]==0:
                            sheet[testy][testx][0]=sheet[y][x][0]
                            sheet[y][x][0]=0
                            y=testy
                            x=testx
                        elif sheet[testy][testx][0]!=sheet[y][x][0]:
                            break
                        elif sheet[testy][testx][0]!=0 and sheet[testy][testx][0]==sheet[y][x][0]:
                            if sheet[testy][testx][1]==0: # 합체
                                sheet[testy][testx][1]=1 # 상태값 변경
                                sheet[testy][testx][0]=sheet[y][x][0]*2
                                sheet[y][x][0]=0
                                break
                            elif sheet[testy][testx][1]==1:
                                break
    elif S==2:
        testy=0
        testx=1
        originy=0
        for y in range(N):
            originy=y
            for x in range(1,N):
                y=originy
                for z in range(N):
                    testy=y+dy[2]
                    testx = x + dx[2]
                    if N > testy > -1 and N > testx > -1:
                        if N>testy>-1 and sheet[testy][testx][0]==0:
                            sheet[testy][testx][0]=sheet[y][x][0]
                            sheet[y][x][0]=0
                            y=testy
                            x=testx
                        elif sheet[testy][testx][0]!=sheet[y][x][0]:
                            break
                        elif sheet[testy][testx][0]!=0 and sheet[testy][testx][0]==sheet[y][x][0]:
                            if sheet[testy][testx][1]==0: # 합체
                                sheet[testy][testx][1]=1 # 상태값 변경
                                sheet[testy][testx][0]=sheet[y][x][0]*2
                                sheet[y][x][0]=0
                                break
                            elif sheet[testy][testx][1]==1:
                                break
    elif S==3:
        testy=0
        testx=N-2
        originy=0
        for y in range(N):
            originy=y
            for x in range(N-2,-1,-1):
                y=originy
                for z in range(N):
                    testy=y+dy[3]
                    testx = x + dx[3]
                    if N > testy > -1 and N > testx > -1:
                        if N>testy>-1 and sheet[testy][testx][0]==0:
                            sheet[testy][testx][0]=sheet[y][x][0]
                            sheet[y][x][0]=0
                            y=testy
                            x=testx
                        elif sheet[testy][testx][0]!=sheet[y][x][0]:
                            break
                        elif sheet[testy][testx][0]!=0 and sheet[testy][testx][0]==sheet[y][x][0]:
                            if sheet[testy][testx][1]==0: # 합체
                                sheet[testy][testx][1]=1 # 상태값 변경
                                sheet[testy][testx][0]=sheet[y][x][0]*2
                                sheet[y][x][0]=0
                                break
                            elif sheet[testy][testx][1]==1:
                                break

    print('#{}'.format(i+1))
    for j in range(len(sheet)):
        for k in sheet[j]:
            print(k[0],end=" ")
        print()

    #cnt를 초기화 시켜두고, 합체될 시 cnt를 증가시켜 합체를 더 못하게함.
