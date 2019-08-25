import sys
sys.stdin=open("pal1.txt",  'rt', encoding='UTF8')


for i in range(10):
    N=int(input())
    map=[[x for x in input()]for y in range(8)]
    ans=0
    for k in range(8):
        for j in range(8 -N + 1):
            text=''
            pal=''
            for u in range(N):
                text+=map[k][u+j]
                pal+=map[k][N-1-u+j]
            if text==pal:
                ans+=1
    for k in range(8):
        for j in range(8 - N + 1):
            text=''
            pal=''
            for u in range(N):
                text+=map[u+j][k]
                pal+=map[N-1-u+j][k]
            if text==pal:
                ans+=1
    print('#{} {}'.format(i+1,ans))