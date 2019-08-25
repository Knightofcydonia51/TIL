import sys
sys.stdin=open("pal2.txt",  'rt', encoding='UTF8')


for i in range(10):
    N=int(input())
    map=[[x for x in input()]for y in range(100)]
    ans=0
    for y in range(100):
        for k in range(99,0,-1):
            for j in range(100-k):
                pal = ''
                text = ''
                for m in range(j): # 98 2 /0 /1
                    text+=ans[y][m+j]
                    pal+=ans[y][k+m+j-1]