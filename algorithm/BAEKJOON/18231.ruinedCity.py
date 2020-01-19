import sys
sys.stdin=open('18231.ruinedCity.txt')

# numbers를 차례차례 순회하며 폭탄을 투하한다.
# 해당 도시와 해당 도시에 연결된 도시들이 만약 numbers에 하나 이상 포함되면서, numbers에 들어있지 않은 도시는 파괴하지 않는다면,
# 해당되는 도시들을 set(ruined)에 넣고 해당 numbers는 답이 될 리스트에 넣는다.
# 반복해서, ruined가 numbers랑 동일하게 되면 ans를 출력한다. 만약 ans가 비어있다면 -1출력

def val(i):
    global flag
    tmplist = []
    for k in range(N):
        if G[i][k]==1 or i==k:
            if k+1 not in numbers:
                return
            else:
                tmplist.append(k + 1)
    cnt=0
    for k in range(len(tmplist)):
        if tmplist[k] in ruined:
            cnt+=1
            continue
        else:
            ruined.append(tmplist[k])
    if cnt==len(tmplist):
        return
    else:
        ans.append(i+1)
    if len(ruined)==len(numbers):
        print(len(ans))
        for k in range(len(ans)):
            print(ans[k],end=" ")
        flag+=1

N,M=map(int,input().split())

info=[list(map(int,input().split())) for y in range(M)]
G=[[0 for x in range(N)]for i in range(N)]


for i in range(M):
    G[info[i][0]-1][info[i][1]-1]=1
    G[info[i][1]-1][info[i][0]-1]=1

K=int(input())
numbers=[int(x) for x in input().split()]

ruined=[]
ans=[]
flag=0

for i in range(len(numbers)):
    if flag==1:
        break
    val(numbers[i]-1)
if not ans:
    print(-1)
