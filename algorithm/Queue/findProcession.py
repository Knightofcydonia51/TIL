import sys
sys.stdin=open('findProcession.txt')




dx=[0,0,-1,1]
dy=[-1,1,0,0]
def dfs(y, x):
    global flag
    visited[y][x] = flag
    for i in range(4):
        testy=y+dy[i]
        testx=x+dx[i]
        if -1<testy<n and -1<testx<n and visited[testy][testx]==0 and pro[testy][testx]!=0:
            dfs(testy,testx)

T = int(input())
for i in range(T):
    n=int(input())
    pro=[[int(x) for x in input().split()]for y in range(n)]
    visited=[[0 for x in range(n)]for y in range(n)]
    numbers=[]
    ans=[]
    flag=1
    for j in range(len(pro)):
        for k in range(len(pro)):
            if pro[j][k]!=0 and visited[j][k]==0:
                numbers.append(flag)
                dfs(j,k)
                flag+=1

    for z in range(len(numbers)):
        temp = []
        for y in range(len(visited)):
            for x in range(len(visited)):
                if visited[y][x]==numbers[z]:
                    temp.append(y);temp.append(x)
        ans.append(temp[-2]-temp[0]+1); ans.append(temp[-1]-temp[1]+1)

    for z in range(len(ans)//2,0,-1):
        for s in range(0,len(ans)-2,2):
            if ans[s]*ans[s+1]>ans[s+2]*ans[s+3]:
                ans[s],ans[s+1],ans[s + 2],ans[s + 3]=ans[s + 2],ans[s + 3],ans[s],ans[s+1]
            elif ans[s]*ans[s+1]==ans[s+2]*ans[s+3]:
                if ans[s]<ans[s+2]:
                    pass
                elif ans[s+2]<ans[s]:
                    ans[s], ans[s + 1], ans[s + 2], ans[s + 3] = ans[s + 2], ans[s + 3], ans[s], ans[s + 1]

    print('#{} {}'.format(i+1, len(numbers)),end=" ")
    for j in range(len(ans)):
        print(ans[j], end=" ")
    print()



