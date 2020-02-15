import sys
sys.stdin=open('2115.getHoney.txt')

T=int(input())

def powerset(k):
    global maxi
    if k==M:
        honey=[]
        limit=0
        for i in range(M):
            if T[i]==1:
                honey.append(worker[i])
                limit+=worker[i]
                if limit>C:
                    return

        honeyWeight=0
        if honey:
            for i in range(len(honey)):
                honeyWeight+=(honey[i]**2)
            if maxi<honeyWeight:
                maxi=honeyWeight

    else:
        T[k]=1
        powerset(k+1)
        T[k]=0
        powerset(k+1)

for i in range(T):
    N, M, C = map(int, input().split())
    sheet=[[int(x) for x in input().split()]for y in range(N)]
    honeyList=[]
    for y in range(N):
        for x in range(N-M+1):
            maxi = 0
            worker=[]
            for n in range(M):
                worker.append(sheet[y][x+n])
            T = [0] * M
            powerset(0)
            honeyList.append([maxi,y,x])
    honeyList=sorted(honeyList,reverse=True)
    ans=0

    for y in range(len(honeyList)):
        for x in range(y+1,len(honeyList)):
            if honeyList[y][1]==honeyList[x][1]:
                if honeyList[y][2]-1<honeyList[x][2]<honeyList[y][2]+M or honeyList[x][2]-1<honeyList[y][2]<honeyList[x][2]+M:
                    continue
                else:

                    if honeyList[y][0]+honeyList[x][0]>ans:
                        ans=honeyList[y][0]+honeyList[x][0]
            else:
                if honeyList[y][0] + honeyList[x][0] > ans:
                    ans = honeyList[y][0] + honeyList[x][0]

    print("#{} {}".format(i+1,ans))
