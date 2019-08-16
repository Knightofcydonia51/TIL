import sys
sys.stdin=open("05.color.txt")

T=int(input())
for i in range(T):
    N=int(input())
    sheet=[[0 for x in range(10)] for y in range(10)]
    minx=11
    maxy=0
    purple=0
    for k in range(N):
        color=[int(x) for x in input().strip().split()]
        if color[0]<minx:
            minx=color[0]
        if color[3]>maxy:
            maxy=color[3]
        for j in range(color[1],color[3]+1):
            for u in range(color[0],color[2]+1):
                if color[4]==1:
                    sheet[j][u]+=1
                else:
                    sheet[j][u]+=2
    for y in range(minx,maxy+1):
        for x in range(minx,maxy+1):
            if sheet[y][x]==3:
                purple+=1
    print('#{} {}'.format(i+1, purple))



