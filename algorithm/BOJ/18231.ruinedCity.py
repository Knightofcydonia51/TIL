import sys
sys.stdin=open('18231.ruinedCity.txt')

def val(i):
    global ans
    global flag
    tmplist=[]
    for k in range(1,len(G)):
        if G[i][k]==1:
            if k in ruined:
                tmplist.append(k)
            else:
                return
        elif i==k:
            if i in ruined:
                tmplist.append(k)
            else:
                return

    for k in range(len(tmplist)):
        destroyed.add(tmplist[k])
    numlist.append(i)
    if len(destroyed)==len(ruined):
        flag+=1
        ans=len(numlist)
        print(ans)
        for j in range(len(numlist)):
            print(numlist[j],end=" ")
        return

N,M=map(int,input().split())

info=[list(map(int,input().split())) for y in range(M)]
K=int(input())
ruined=[int(x) for x in input().split()]
G=[[0 for x in range(N+1)]for i in range(N+1)]
destroyed=set([])
numlist=[]

flag=0
ans= -1

for i in range(M):
    G[info[i][0]][info[i][1]]=1
    G[info[i][1]][info[i][0]]=1

for i in range(len(ruined)):
    if flag==1:
        break
    val(ruined[i])

if flag==0:
    print(ans)