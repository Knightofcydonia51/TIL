import sys
sys.stdin=open('14503.robotCleaner.txt')

def cleaning(y,x,d):
    global clean
    cleaned[y][x] = 1
    clean+=1
    val=0
    # 북 동 남 서 0 1 2 3
    for i in [1,0],[-1,0],[0,-1],[0,1]:
        ny=y+i[0]
        nx=x+i[1]
        if sheet[ny][nx]==1 or cleaned[ny][nx]==1:
            val+=1
    if val<4:
        if d == 0:  # 북
            if cleaned[y][x - 1] == 0 and sheet[y][x - 1] == 0:
                cleaning(y, x - 1, 3)
            elif cleaned[y][x - 1] == 1 or sheet[y][x - 1] == 1:
                clean-=1
                cleaning(y, x, 3)
        elif d==1: # 동
            if cleaned[y-1][x] == 0 and sheet[y-1][x] == 0:
                cleaning(y-1,x, 0)
            elif cleaned[y - 1][x] == 1 or sheet[y - 1][x] == 1:
                clean -= 1
                cleaning(y, x, 0)
        elif d==2: #남 
            if cleaned[y][x +1] == 0 and sheet[y][x + 1] == 0:
                cleaning(y, x + 1, 1)
            elif cleaned[y][x +1] == 1 or sheet[y][x + 1] == 1:
                clean -= 1
                cleaning(y, x, 1)
        else: #서
            if cleaned[y+1][x] == 0 and sheet[y+1][x] == 0:
                cleaning(y+1, x, 2)
            elif cleaned[y+1][x] == 1 or sheet[y+1][x] == 1:
                clean -= 1
                cleaning(y, x, 2)

    elif val==4:
        if d==0:
            if sheet[y+1][x]==1:
                return
            else:
                clean-=1
                cleaning(y+1,x,0)
        elif d==1:
            if sheet[y][x-1]==1:
                return
            else:
                clean -= 1
                cleaning(y,x-1,1)
        elif d==2:
            if sheet[y-1][x] == 1:
                return
            else:
                clean -= 1
                cleaning(y-1,x,2)
        elif d==3:
            if sheet[y][x+1] == 1:
                return
            else:
                clean -= 1
                cleaning(y,x+1,3)

N,M=map(int,input().split())
r,c,d=map(int,input().split())
sheet=[[int(x) for x in input().split()]for y in range(N)]
cleaned=[[0 for x in range(M)]for y in range(N)]
clean=0
cleaning(r,c,d)
print(clean)
