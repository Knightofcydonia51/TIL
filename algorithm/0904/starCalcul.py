import sys
sys.stdin=open("starCalcul.txt")

sheet=[[0 for x in range(295)]for y in range(295)]
cnt=1
for z in range(1,293):
    x=z
    for y in range(z,0,-1):
        sheet[y][x-y+1]=cnt
        cnt+=1

T=int(input())

for i in range(T):
    ans=0
    p,q=map(int,input().split())
    ploca,qloca=[],[]
    for z in range(1, 293):
        if len(ploca)!=0 and len(qloca)!=0:
            ans = sheet[ploca[0] + qloca[0]][ploca[1] + qloca[1]]
            break
        x = z
        for y in range(z, 0, -1): #x=1 y=1 z=1
            if sheet[y][x - y + 1] == p:
                ploca=[y,x - y + 1]
            if sheet[y][x - y + 1] ==q:
                qloca=[y,x-y+1]
    print('#{} {}'.format(i+1,ans))