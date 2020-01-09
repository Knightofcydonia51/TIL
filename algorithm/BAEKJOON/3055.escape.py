import collections
import sys
sys.stdin=open('3055.escape.txt')

dyx=[[-1,0],[1,0],[0,-1],[0,1]]

def dead(y,x,d):
    cnt=0
    for i in range(4):
        ny,nx=y+dyx[i][0],x+dyx[i][1]
        if -1<ny<R and -1<nx<C and sheet[ny][nx]!='X':
            if sheet[ny][nx]=='*':
                cnt+=1
    if d==cnt:
        return cnt

def waterDelta(y,x):
    for i in range(4):
        ny,nx=y+dyx[i][0],x+dyx[i][1]
        if -1<ny<R and -1<nx<C and sheet[ny][nx]=='.':
            floor.append((ny,nx))
            sheet[ny][nx]='*'

def moleDelta(y,x):
    global flag
    for i in range(4):
        ny, nx = y + dyx[i][0], x + dyx[i][1]
        if -1 < ny < R and -1 < nx < C and visit[ny][nx]==0 and sheet[ny][nx]!='X' and sheet[ny][nx]!='*':
            if sheet[ny][nx]=='D':
                flag+=1
                return
            else:
                move.append((ny, nx))
                visit[ny][nx]=1

def start():
    for y in range(R):
        for x in range(C):
            if sheet[y][x] == 'S':
                mole.append((y, x))
                sheet[y][x]='.'
            if sheet[y][x] == '*':
                water.append((y, x))
            if sheet[y][x]=='D':
                home.append((y,x))

R, C = map(int,input().split())

sheet=[[x for x in input()]for y in range(R)]
visit=[[0 for x in range(C)]for y in range(R)]

flag=0
minute=0
mole = collections.deque([])
water = collections.deque([])
home=[]
deadFlag=0

start()

for i in range(4):
    ny, nx = home[0][0] + dyx[i][0], home[0][1] + dyx[i][1]
    if -1 < ny < R and -1 < nx < C and sheet[ny][nx] != 'X':
        deadFlag+=1

while 1:
    move = collections.deque([])
    floor = collections.deque([])
    minute+=1
    while water:
        y,x=water.popleft()
        waterDelta(y,x)
    water=floor

    while mole:
        y,x=mole.popleft()
        moleDelta(y,x)
        if flag==1:
            break
    if flag==1:
        print(minute)
        break
    mole=move
    if not mole:
        print("KAKTUS")
        break
    if deadFlag==dead(home[0][0],home[0][1],deadFlag):
        print("KAKTUS")
        break





