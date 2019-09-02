import sys
sys.stdin=open('magnatic.txt')


'''
5
1 1 0 2 2
0 2 0 1 1
0 0 0 0 0
0 1 0 0 0
0 0 2 0 0
'''


for i in range(10):
    N=int(input())
    sheet=[[int(x) for x in input().split()]for y in range(N)] #1은 N극 (밑으로) 2는 S극 (위로)
    for z in range(len(sheet)):
        cnt = 0
        for y in range(N-1,-1,-1):
            for x in range(len(sheet)):
                if sheet[y][x]==1:
                    if y == N - 1 and sheet[y - 1][x] != 2:
                        sheet[y][x] = 0
                    elif -1<y<N-1 and sheet[y+1][x]==0:
                        sheet[y][x]=0
                        sheet[y+1][x]=1
                    elif -1 < y < N-1 and sheet[y+1][x]!=0:
                        if sheet[y+1][x]==1:
                            pass
                        elif sheet[y + 1][x] == 2:
                            cnt+=1
        for j in range(len(sheet)):
            for k in range(len(sheet)):
                if sheet[j][k]==2:
                    if j == 0 and sheet[j+1][k]!=1:
                        sheet[j][k] = 0
                    elif -1<j<N-1 and sheet[j-1][k]==0:
                        sheet[j][k] = 0
                        sheet[j-1][k]=2
                    elif -1<j<N-1 and sheet[j-1][k]!=0:
                        if sheet[j-1][k]==2:
                            pass
                        elif sheet[j-1][k]==1:
                            pass
    print('#{} {}'.format(i+1,cnt))

