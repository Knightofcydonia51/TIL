import sys
sys.stdin=open('8979.olympic.txt')


N,K = map(int,input().split())
nations=[]
rank=1

for i in range(N):
    nation=[int(x) for x in input().split()]
    if nation[0]==K:
        gold=nation[1]
        sliver=nation[2]
        bronze=nation[3]
    nations.append(nation)

for i in range(N):
    if nations[i][1]>gold:
        rank+=1
    elif nations[i][1]==gold:
        if nations[i][2]>sliver:
            rank+=1
        elif nations[i][2]==sliver:
            if nations[i][3]>bronze:
                rank+=1
            elif nations[i][3]==bronze:
                continue
            else:
                continue
        else:
            continue
    else:
        continue

print(rank)
