import sys
sys.stdin=open('01.txt')


T=int(input())
for i in range(T):
    N=int(input())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    maxi=0
    lowestCost=98765
    same=[]
    for y in range(N):
        for z in range(N):
            validate = []
            dict = {}
            cost=0
            for x in range(N): #둘다 있을떄, A는 있고 B는 없을때, B는 있고 A는 없을때, 둘다 없을때
                if N-x-1==y:
                    validate.append(sheet[y][x])
                    continue
                else:
                    validate.append(sheet[y][x])
                    validate.append(sheet[N-x-1][z])
            for k in range(len(validate)):
                if validate[k] in dict:
                    dict[validate[k]]+=1
                else:
                    dict[validate[k]]=1
            lowcost = 98765
            lowkey=0
            for key in dict.items(): #코스트검증
                cost=0
                for k in range(len(validate)):
                    if validate[k]!=key[0]:
                        cost+=abs(key[0]-validate[k])
                if cost<=lowcost:
                    lowcost=cost
                    lowkey=key[0]
            if lowcost<=lowestCost:
                lowestCost=lowcost
                same.append((lowestCost,lowkey))
    realLow=min([x[0] for x in same])
    lowlowkey=6
    for k in range(len(same)):
        if same[k][0]==realLow and same[k][1]<lowlowkey:
            lowlowkey=same[k][1]
    print('#{} {} {}'.format(i+1,realLow,lowlowkey))

