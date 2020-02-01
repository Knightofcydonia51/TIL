import sys
sys.stdin=open('2823.U_turn.txt')



def val():
    global flag
    for y in range(R):
        for x in range(C):
            if sheet[y][x]=='.':
                cnt=0
                for i in [1,0],[-1,0],[0,1],[0,-1]:
                    ny=y+i[0]
                    nx=x+i[1]
                    if -1<ny<R and -1<nx<C and sheet[ny][nx]=='.':
                        cnt+=1
                if cnt<=1:
                    flag+=1
                    return


R,C = map(int,input().split())
sheet=[[x for x in input()]for y in range(R)]
visited=[[0 for x in range(C)]for y in range(R)]
flag=0
val()
print(flag)







