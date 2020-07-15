import sys
sys.stdin=open('1996_mine.txt')

def mine(y,x):
    mine_num=sheet[y][x]
    for i in range(y-1,y+2,1):
        for k in range(x-1,x+2):
            if N>i>=0 and N>k>=0:
                if type(sheet[i][k]) != str:
                    if sheet[i][k]<100:
                        sheet[i][k]+=(mine_num//100)
                        if sheet[i][k]>9:
                            sheet[i][k]='M'
    sheet[y][x]='*'

N=int(input())
sheet2=[[str(x) for x in input()]for y in range(N)]
sheet=[]
for s in sheet2:
    sheet.append(list(map(lambda x:0 if x=='.' else 100*int(x), s)))

for i in range(len(sheet)):
    for k in range(len(sheet)):
        if type(sheet[i][k])!=str:
            if sheet[i][k]>=100:
                mine(i,k)

for i in range(len(sheet)):
    for k in range(len(sheet)):
        print(sheet[i][k],end="")
    print()





