import sys
sys.stdin=open('othello.txt')

dy=[0,-1,-1,-1,0,1,1,1] #좌 좌상 상 우상 우 우하 하 좌하
dx=[-1,-1,0,1,1,1,0,-1]

def sonar(ty,tx,way,color):
    global cnt
    if cnt==0:
        return

    for i in range(cnt):
        if color==1:
            print("hiiiiiiiiiiiiiiiii",cnt,ty,tx,way)
            sheet[ty+(dy[way]*(-1))][tx+(dx[way]*(-1))]=1
            ty=ty+(dy[way]*(-1))
            tx=tx+(dx[way]*(-1))
        elif color == 2:
            print("hii222222222", cnt, ty, tx, way)
            sheet[ty + (dy[way] * (-1))][tx + (dx[way] * (-1))]=2
            ty = ty + (dy[way] * (-1))
            tx = tx + (dx[way] * (-1))

T=int(input())

for i in range(T):
    N,M=map(int,input().split())
    sheet=[[0 for x in range(N)]for y in range(N)]
    sheet[N//2][N//2]=2; sheet[N//2-1][N//2-1]=2 #1이면 흑, 2면 백
    sheet[N//2-1][N//2]=1; sheet[N//2][N//2-1]=1
    for j in range(M):
        x,y,bw=map(int,input().split()) #1(x=0),2(y=1) = (y=1,x=0)
        x-=1; y-=1
        originx=x; originy=y
        sheet[originy][originx]=bw
        [print(sheet[z]) for z in range(len(sheet))]
        print()
        for k in range(8):
            cnt = 0
            for u in range(N):
                testy=y+dy[k]
                testx=x+dx[k]
                # print(y,x, testy, testx)
                if -1<testy<N and -1<testx<N:
                    if sheet[testy][testx]==0:
                        break
                    elif sheet[testy][testx]==bw:
                        sonar(testy,testx,k,bw)
                        x=originx; y=originy
                        break
                    elif sheet[testy][testx]!=0 and sheet[testy][testx]!=bw:
                        y=testy
                        x=testx
                        cnt+=1
                elif testx==-1 or testy==-1 or testx==N or testy==N:
                    break

    # print(sheet)
