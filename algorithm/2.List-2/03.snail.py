# import sys
# sys.stdin=open("03.snail.txt")


def isWall(x,y):
    if x!=0 : return True
    if y!=0 : return True
    return False

def forward(step,X,Y,d,road):
    if d==0: #right
        X+=1; step+=1
        road[Y][X]=step
    elif d==1: #down
        Y+=1; step+=1
        road[Y][X]=step
    elif d==2: #left
        X-=1; step+=1
        road[Y][X]=step
    elif d==3: #up
        Y-=1; step+=1
        road[Y][X]=step

T=int(input())
for i in range(T):
    N=int(input())
    arr =[[0]*N]*N
    handle=[0,1,2,3]
    direction=(-1)
    arr[0][0]=1
    global step;
    step = 1
    global x;
    x = 0
    global y;
    y = 0
    for k in range(3):
        direction+=1
        for j in range(N - 1):
            forward(step,x,y,direction%4, arr)
    print(arr)

