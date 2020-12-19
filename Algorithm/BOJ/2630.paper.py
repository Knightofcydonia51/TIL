import sys
sys.stdin=open('test.txt')



def val(y,x,N):
    global blue, white
    color=sheet[y][x]

    if N==1:
        pass
    
    else:
        for ny in range(N):
            for nx in range(N):
                if sheet[y+ny][x+nx] != color:
                    val(y,x,N//2)
                    val(y,x+N//2,N//2)
                    val(y+N//2,x,N//2)
                    val(y+N//2,x+N//2,N//2)
                    return

    if color=="1":
        blue+=1
    else:
        white+=1


N=int(input())
sheet=[[i for i in input().split()] for y in range(N)]

blue=0
white=0
val(0,0,N)
print(white, end="\n")
print(blue)
